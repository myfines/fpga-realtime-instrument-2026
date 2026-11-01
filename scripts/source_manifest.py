"""Write or verify the source delivery SHA-256 manifest (no device access)."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / 'SOURCE-MANIFEST.json'

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write', action='store_true', help='Refresh from non-ignored Git files')
    args = parser.parse_args()
    if args.write:
        result = subprocess.check_output(
            ['git', '-C', str(ROOT), 'ls-files', '--cached', '--others', '--exclude-standard', '-z'])
        names = sorted(set(n.decode('utf-8') for n in result.split(b'\0') if n))
        data = {}
        for name in names:
            if name == MANIFEST.name or Path(name).suffix.lower() in {'.keystore', '.jks'}:
                continue
            file = ROOT / name
            if file.is_file():
                data[name] = digest(file)
        MANIFEST.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        print(f'Wrote {len(data)} file hashes')
    data = json.loads(MANIFEST.read_text(encoding='utf-8'))
    failures = []
    for name, expected in data.items():
        file = (ROOT / name).resolve()
        if ROOT.resolve() not in file.parents or not file.is_file() or digest(file) != expected:
            failures.append(name)
    if failures:
        raise SystemExit('Manifest verification failed: ' + ', '.join(failures))
    print(f'PASS: {len(data)} source files match SHA-256 manifest')

if __name__ == '__main__':
    main()
