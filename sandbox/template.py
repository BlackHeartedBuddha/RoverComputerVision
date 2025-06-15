import cv2
import torch
from ultralytics import YOLO

# Check for available CUDA devices
gpu_count = torch.cuda.device_count()
device_index = "cpu"
print("CUDA Available:", torch.cuda.is_available())
print("Device Count:", torch.cuda.device_count())
print("GPU Name:", torch.cuda.get_device_name(0) if torch.cuda.is_available() else "N/A")


if gpu_count > 0:
    print(f"✅ {gpu_count} CUDA device(s) available:\n")
    for i in range(gpu_count):
        print(f"[{i}] {torch.cuda.get_device_name(i)}")
    print(f"[c] Use CPU instead")

    # Prompt user to select device
    selected = input(f"\nSelect GPU index (0–{gpu_count - 1}) or 'c' for CPU: ").strip()

    if selected.lower() == "c":
        device_index = "cpu"
    else:
        try:
            selected_int = int(selected)
            if 0 <= selected_int < gpu_count:
                device_index = selected_int
            else:
                print("❌ Invalid GPU index. Using CPU.")
                device_index = "cpu"
        except ValueError:
            print("❌ Invalid input. Using CPU.")
            device_index = "cpu"
else:
    print("⚠️ No CUDA-compatible GPU found. Using CPU.")

# Load the YOLOv8 model
model = YOLO("yolov8n.pt")  # or yolov8s.pt, yolov8m.pt...

# Open the default webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("❌ Error: Could not open webcam.")
    exit()

print(f"\n🎥 Using device: {device_index}")
print("Press 'q' to quit.\n")

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ Failed to grab frame.")
        break

    # Run YOLO inference on the selected device
    results = model(frame, stream=True, device=device_index)

    for r in results:
        annotated_frame = r.plot()

    cv2.imshow("YOLOv8 Detection", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
