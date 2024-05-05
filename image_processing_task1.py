import cv2
import numpy as np
import os
import matplotlib.pyplot as plt
import random

def display_images_and_histograms(images, titles):
    """Displays images with their color channel histograms."""
    plt.figure(figsize=(15, 9))

    for i in range(len(images)):
        image = images[i]
        title = titles[i]

        plt.subplot(3, 4, i * 4 + 1)
        plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        plt.title(title)
        plt.axis('off')

        hist_b = cv2.calcHist([image], [0], None, [256], [0, 256])
        hist_g = cv2.calcHist([image], [1], None, [256], [0, 256])
        hist_r = cv2.calcHist([image], [2], None, [256], [0, 256])

        plt.subplot(3, 4, i * 4 + 2)
        plt.plot(hist_b, color='blue')
        plt.title('Blue Channel Histogram')
        plt.xlabel('Pixel Value')
        plt.ylabel('Frequency')

        plt.subplot(3, 4, i * 4 + 3)
        plt.plot(hist_g, color='green')
        plt.title('Green Channel Histogram')
        plt.xlabel('Pixel Value')
        plt.ylabel('Frequency')

        plt.subplot(3, 4, i * 4 + 4)
        plt.plot(hist_r, color='red')
        plt.title('Red Channel Histogram')
        plt.xlabel('Pixel Value')
        plt.ylabel('Frequency')

    plt.tight_layout()


def adjust_contrast(image, alpha):
    return cv2.convertScaleAbs(image, alpha=alpha, beta=0)


def adjust_brightness(image, beta):
    return cv2.convertScaleAbs(image, alpha=1.0, beta=beta)


def save_image(image):
    """Saves the image based on user input."""
    save_option = input("Do you want to save the resulting image? (yes/no): ").lower()
    if save_option == 'yes':
        filename = input("Enter the filename to save (with extension, e.g., result.jpg): ")
        cv2.imwrite(filename, image)
        print(f"Image saved as {filename}")
    elif save_option == 'no':
        print("Image not saved.")
    else:
        print("Invalid option. Image not saved.")


def main():
    """Prompts the user for an image path, loads the image, performs operations, and displays results."""

    while True:
        # Ask user to input image path
        while True:
            image_path = input("Enter the path to the image: ")
            if not image_path:
                print("Please enter a valid image path.")
                continue

            # Check if the file exists
            if not os.path.isfile(image_path):
                print(f"Error: File '{image_path}' does not exist. Please try again.")
                continue

            break  # Exit the loop if a valid path is provided

        # Load the image
        image = cv2.imread(image_path)

        # Check if the image was loaded correctly
        if image is None:
            print(f"Error loading image from {image_path}. Check the file path and permissions.")
            return

        # Generate random values for contrast and brightness adjustment
        random_contrast = random.uniform(0.5, 2.0)  # Random value between 0.5 and 2.0
        random_brightness = random.randint(-100, 100)  # Random integer value between -100 and 100

        # Prepare adjusted images
        contrast_adjusted_image = adjust_contrast(image.copy(), random_contrast)
        brightness_adjusted_image = adjust_brightness(image.copy(), random_brightness)

        # Prepare titles for display
        titles = ['Original Image', f'Contrast Adjusted (Factor: {random_contrast:.2f})', f'Brightness Adjusted (Beta: {random_brightness})']

        # Display images and histograms
        display_images_and_histograms([image, contrast_adjusted_image, brightness_adjusted_image], titles)
        plt.show()

        # Save resulting image
        save_image(brightness_adjusted_image)  # You can choose any of the adjusted images here

        # Ask user if they want to try again or finish the program
        repeat_option = input("Do you want to try again? (yes/no): ").lower()
        if repeat_option != 'yes':
            print("Program finished.")
            break


if __name__ == "__main__":
    main()
