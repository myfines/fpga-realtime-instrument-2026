"""K230 SD-card startup entry for the included UART gesture sender."""
with open("/sdcard/uart_gesture_sender_standalone.py") as source_file:
    source = source_file.read()
exec(compile(source, "/sdcard/uart_gesture_sender_standalone.py", "exec"), {"__name__": "__main__"})
