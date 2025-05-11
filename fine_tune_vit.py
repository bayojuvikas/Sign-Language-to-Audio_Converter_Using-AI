import os
from datasets import load_dataset
from transformers import ViTForImageClassification, TrainingArguments, Trainer
from transformers import ViTFeatureExtractor, DefaultDataCollator
from PIL import Image
import numpy as np
import evaluate

# Load dataset
dataset = load_dataset('imagefolder', data_dir='C:/Users/umad3/resized_data')

# Define feature extractor
feature_extractor = ViTFeatureExtractor.from_pretrained('google/vit-base-patch16-224-in21k')

# Preprocessing function
def preprocess_images(examples):
    images = []
    for image_file in examples['image']:
        try:
            image = Image.open(image_file).convert("RGB")
            images.append(np.array(image))
        except Exception as e:
            print(f"Error loading image {image_file}: {e}")
            images.append(None)  # Placeholder for failed image
    inputs = feature_extractor(images, return_tensors='pt')
    return inputs

# Apply preprocessing
dataset = dataset.map(preprocess_images, batched=True)

# Load metric
accuracy = evaluate.load("accuracy", trust_remote_code=True)

# Define the model
model = ViTForImageClassification.from_pretrained('google/vit-base-patch16-224-in21k', num_labels=5)

# Define training arguments
training_args = TrainingArguments(
    output_dir="./vit-gesture",
    per_device_train_batch_size=8,
    evaluation_strategy="epoch",
    num_train_epochs=4,
    save_steps=500,
    save_total_limit=2,
    remove_unused_columns=False,
    push_to_hub=False,
)

# Define data collator
data_collator = DefaultDataCollator()

# Define the trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset["train"],
    eval_dataset=dataset["validation"],
    data_collator=data_collator,
    tokenizer=feature_extractor,
    compute_metrics=lambda p: {"accuracy": accuracy.compute(predictions=np.argmax(p.predictions, axis=1), references=p.label_ids)},
)

# Train the model
trainer.train()

# Save the model
trainer.save_model("vit-gesture")
