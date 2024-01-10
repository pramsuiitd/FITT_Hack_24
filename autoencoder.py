import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pandas as pd

# Load the generated dataset
df = pd.read_csv('ddos_dataset.csv')

# Extract features and labels
features = df.iloc[:, 2:8].values
labels = df.iloc[:, 8].values

# Split the dataset into training and testing sets
train_features, test_features, train_labels, test_labels = train_test_split(
    features, labels, test_size=0.2, random_state=42
)

# Standardize features
scaler = StandardScaler()
train_features = scaler.fit_transform(train_features)
test_features = scaler.transform(test_features)

# Convert to PyTorch tensors
train_tensor = torch.Tensor(train_features)
test_tensor = torch.Tensor(test_features)

# Create DataLoader
train_dataset = TensorDataset(train_tensor, train_tensor)
train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)

validation_dataset = TensorDataset(test_tensor, test_tensor)
validation_loader = DataLoader(validation_dataset, batch_size=32, shuffle=False)

# Define Autoencoder model
class Autoencoder(nn.Module):
    def __init__(self):
        super(Autoencoder, self).__init__()
        self.encoder = nn.Sequential(
            nn.Linear(6, 4),
            nn.ReLU(),
        )
        self.decoder = nn.Sequential(
            nn.Linear(4, 6),
            nn.Sigmoid(),
        )

    def forward(self, x):
        x = self.encoder(x)
        x = self.decoder(x)
        return x

# Initialize the model, loss function, and optimizer
model = Autoencoder()
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Train the Autoencoder
num_epochs = 50
for epoch in range(num_epochs):
    model.train()
    for data in train_loader:
        inputs, _ = data
        outputs = model(inputs)

        loss = criterion(outputs, inputs)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    # Validation
    model.eval()
    total_loss = 0.0
    with torch.no_grad():
        for data in validation_loader:
            inputs, _ = data
            outputs = model(inputs)
            total_loss += criterion(outputs, inputs).item()

    average_loss = total_loss / len(validation_loader)

    print(f'Epoch [{epoch+1}/{num_epochs}], Validation Loss: {average_loss:.4f}')
# Save the trained model
    
threshold = 0.5

# Evaluate on test data
with torch.no_grad():
    test_tensor = torch.Tensor(test_features)
    outputs = model(test_tensor)
    test_loss = nn.MSELoss(reduction='none')(outputs, test_tensor)

# Classify instances based on the threshold
predictions = (test_loss > threshold).float().numpy()

# Calculate accuracy
accuracy = sum(predictions == test_labels) / len(test_labels)
torch.save(model.state_dict(), 'autoencoder_model.pth')
