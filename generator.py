import csv
import random
from faker import Faker

faker = Faker()

def generate_random_nodes(num_nodes):
    """Generate a list of random node addresses (UUIDs)."""
    return [faker.uuid4() for _ in range(num_nodes)]

def generate_normal_packet(nodes):
    """Generate features for a normal packet."""
    return [
        random.choice(nodes),            # src-id
        random.choice(nodes),            # des-id
        random.randint(1, 20),           # hop count
        random.randint(1024, 65535),     # src-port
        random.randint(1024, 65535),     # des-port
        faker.uuid4(),                   # flow
        random.randint(1, 100),          # packets per flow
        random.randint(100, 2500),       # bytes per flow
        random.uniform(1, 100),          # packet rate
        0                                # Label for normal packet
    ]

def generate_ddos_packet(nodes):
    """Generate features for a DDoS packet."""
    return [
        random.choice(nodes),            # src-id
        random.choice(nodes),            # des-id
        random.randint(10, 30),           # Increase hop count for DDoS
        random.randint(1024, 65535),
        random.randint(1024, 65535),
        faker.uuid4(),
        random.randint(100, 1000),
        random.randint(1000, 5000),       # Increase bytes per flow for DDoS
        random.uniform(50, 300),          # Increase packet rate for DDoS
        1                                 # Label for DDoS packet
    ]

def generate_labeled_dataset(num_samples, output_file):
    """Generate a labeled dataset."""

    nodes = generate_random_nodes(100)

    with open(output_file, 'w', newline='') as csvfile:
        fieldnames = [
            'src-id', 'des-id', 'hop count', 'src-port', 'des-port',
            'packet per flow', 'byte per flow', 'packet rate', 'label'
        ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for _ in range(num_samples):
            if random.random() < 0.9:  # 90% chance of normal packet
                packet = generate_normal_packet(nodes)
            else:
                packet = generate_ddos_packet(nodes)

            writer.writerow({
                'src-id': packet[0],
                'des-id': packet[1],
                'hop count': packet[2],
                'src-port': packet[3],
                'des-port': packet[4],
                'packet per flow': packet[6],
                'byte per flow': packet[7],
                'packet rate': packet[8],
                'label': packet[9]
            })

if __name__ == "__main__":
    num_samples = 100000  # Adjust the number of samples as needed
    output_file = 'ddos_dataset.csv'

    generate_labeled_dataset(num_samples, output_file)
    print(f"Labeled dataset created and saved to {output_file}.")
