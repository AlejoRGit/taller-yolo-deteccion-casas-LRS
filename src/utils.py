import os
import xml.etree.ElementTree as ET

CLASS_MAP = {
    "House": 0
}

def convert_box(size, box):
    dw = 1.0 / size[0]
    dh = 1.0 / size[1]

    xmin, ymin, xmax, ymax = box

    x_center = (xmin + xmax) / 2.0
    y_center = (ymin + ymax) / 2.0
    width = xmax - xmin
    height = ymax - ymin

    return (
        x_center * dw,
        y_center * dh,
        width * dw,
        height * dh
    )

def convert_xml_folder(xml_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    for file in os.listdir(xml_dir):
        if file.endswith(".xml"):
            xml_path = os.path.join(xml_dir, file)
            tree = ET.parse(xml_path)
            root = tree.getroot()

            size = root.find("size")
            w = int(size.find("width").text)
            h = int(size.find("height").text)

            filename = os.path.splitext(file)[0]
            txt_path = os.path.join(output_dir, filename + ".txt")

            with open(txt_path, "w") as f:
                for obj in root.findall("object"):
                    class_name = obj.find("name").text
                    if class_name not in CLASS_MAP:
                        continue

                    class_id = CLASS_MAP[class_name]

                    xml_box = obj.find("bndbox")
                    xmin = float(xml_box.find("xmin").text)
                    ymin = float(xml_box.find("ymin").text)
                    xmax = float(xml_box.find("xmax").text)
                    ymax = float(xml_box.find("ymax").text)

                    yolo_box = convert_box((w, h), (xmin, ymin, xmax, ymax))
                    f.write(f"{class_id} {' '.join(map(str, yolo_box))}\n")


                