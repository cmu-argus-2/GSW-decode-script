import struct
from constants import DATA_FORMAT, FIELDS
import csv

"""
Change this to the data process that you would like to unpack.
Available options are: 
    - adcs
    - cdh
    - cmd_logs
    - comms
    - eps
    - gps

To add more you will need to modify constants.py
"""
log_type = "eps"

def unpack_bin(file_path, output_csv, struct_format):
    """
    Unpacks a binary (.bin) file and writes the extracted data to a CSV file.

    Args:
        file_path (str): Path to the .bin file.
        output_csv (str): Path to the output CSV file.
        struct_format (str): Format string for struct.unpack().

    Returns:
        None
    """
    try:
        # Calculate the size of one record
        record_size = struct.calcsize(struct_format)

        # Determine the number of fields
        num_fields = len(struct.unpack(struct_format, b"\x00" * record_size))

        field_types = struct_format.replace(" ", "")  # Remove spaces if any
        field_sizes = [struct.calcsize(t) for t in field_types]  # Byte sizes per field

        # Generate placeholder field names (e.g., Field_0, Field_1, ...)
        field_names = FIELDS[log_type]

        with open(file_path, "rb") as bin_file, open(output_csv, "w", newline="") as csv_file:
            writer = csv.writer(csv_file)
            
            # Write CSV Header
            writer.writerow(field_names)

            while True:
                # Read the next record from the binary file
                record = bin_file.read(record_size)

                # Stop if no data left
                if len(record) == 0:
                    break

                # Handle partial records
                available_bytes = len(record)
                unpacked_data = []
                offset = 0

                for i, field_type in enumerate(field_types):
                    field_size = struct.calcsize(field_type)

                    # If enough bytes are available, unpack the field
                    if offset + field_size <= available_bytes:
                        field_data = record[offset : offset + field_size]
                        value = struct.unpack(field_type, field_data)[0]  # Unpack single value
                        unpacked_data.append(value)
                    else:
                        unpacked_data.append(None)  # Field missing, add None

                    offset += field_size

                # Write row to CSV
                writer.writerow(unpacked_data)

        print(f"Successfully unpacked '{file_path}' and saved to '{output_csv}'")

    except Exception as e:
        print(f"Error unpacking file: {e}")


# Change below to desired .bin file to unpack
bin_file_to_unpack = "eps_1577841053.bin"
file_path = "../downlinked_bin_files/" + bin_file_to_unpack

# Changle below to desired path to csv file
output_file_name = "output_eps.csv"
output_csv = "../decoded_files/" + output_file_name

struct_format = DATA_FORMAT[log_type]

unpack_bin(file_path, output_csv, struct_format)