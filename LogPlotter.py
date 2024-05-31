import os
import pandas as pd
import matplotlib.pyplot as plt


def read_log_file(file_path):
    data = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            try:
                parts = line.split()
                if len(parts) > 2:
                    magnitude = float(parts[2].strip())
                    data.append(magnitude)
            except ValueError:
                continue
    return data


class LogPlotter:
    def __init__(self, log_file_paths, output_dir):
        self.log_file_paths = log_file_paths
        self.output_dir = output_dir

    def plot_logs(self, filename):
        # Create subplots
        fig, axes = plt.subplots(nrows=4, ncols=4, figsize=(15, 15))

        # Flatten the axes array for easy iteration
        axes = axes.flatten()

        for i in range(len(self.log_file_paths)):
            # Read the file and extract the values
            data = read_log_file(self.log_file_paths[i])

            # Create a DataFrame with the extracted data
            df = pd.DataFrame(data, columns=['Magnitude'])
            df['Frame'] = range(len(df))

            # Plot the data on the respective subplot
            ax = axes[i]
            ax.plot(df['Frame'], df['Magnitude'])
            ax.set_xlabel('Frame')
            ax.set_ylabel('Magnitude')
            ax.set_ylim(0, 100)
            ax.set_title(f'landmark {self.log_file_paths[i].replace(".log", "")}')
            ax.grid(True)

        # Adjust layout
        plt.tight_layout()

        # Save the combined plot as an image file
        os.makedirs(self.output_dir, exist_ok=True)
        plt.savefig(os.path.join(self.output_dir, f'{filename}'))

        plt.show()
        plt.close()

