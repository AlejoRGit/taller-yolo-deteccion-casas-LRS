from utils import convert_xml_folder

convert_xml_folder(
    xml_dir=r"dataset\images\train",
    output_dir=r"dataset\labels\train"
)

convert_xml_folder(
    xml_dir=r"dataset\images\val",
    output_dir=r"dataset\labels\val"
)