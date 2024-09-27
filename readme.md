# Real-Time PCA-based Image Compression and Error Visualization

## Overview

This Python script captures images from a webcam, applies Principal Component Analysis (PCA) for dimensionality reduction (image compression), and visually compares the original image with the reconstructed one. The error between the two is also displayed using a color map to highlight differences.

## Requirements

- **Python 3.x**
- **OpenCV**: `pip install opencv-python`
- **scikit-learn**: `pip install scikit-learn`
- **NumPy**: `pip install numpy`

## How It Works

1. **Capture Images**: The script captures a specified number of images (`n_samples`) from the webcam, converts them to grayscale, and resizes them to a specified quality (`img_quality`).
   
2. **PCA Setup**: The captured images are reshaped and fed into a PCA model with a defined number of components (`n_components1`). PCA compresses the images by projecting them into a lower-dimensional space.

3. **Real-time Compression**: After fitting the PCA model, the script continuously captures new webcam frames. Each frame is resized and projected into the PCA space, and then reconstructed back into its original dimensions.

4. **Error Visualization**: The difference between the original and reconstructed images is visualized using a color map to highlight the compression errors.

## Usage

1. **Parameters**:
   - `n_samples`: The number of images to capture for PCA training.
   - `n_components1`: The number of principal components (eigenvectors) used in PCA. Should be less than or equal to both `n_samples` and `img_quality`.
   - `img_quality`: The resolution of the captured images (both width and height). Should be large enough to ensure quality PCA compression.
   - `out_img_quality`: The display resolution for the output images.

2. **Running the Script**:
   - Ensure your webcam is available and connected.
   - Run the script. It will capture images, apply PCA, and display the original, compressed, and error-highlighted images in separate windows.
   - Press the `q` key to exit the application.

## Error Handling

If either the number of samples (`n_samples`) or image quality (`img_quality`) is less than the number of PCA components (`n_components1`), the script will terminate with an error message. This ensures the input data is sufficient for performing PCA.

You can comment out the line with `exit()` to see the error if desired.

## Visualization

- **Original Image**: Displays the raw image captured from the webcam.
- **Transformed Image**: Displays the PCA-reconstructed image.
- **Error Image**: Shows the difference between the original and PCA-reconstructed images, using a color map for visual emphasis.

## Keyboard Controls

- **Press 'q'**: Exit the program.

## Notes

- PCA-based compression is lossy, meaning some detail from the original image is lost during reconstruction. This loss is visualized in the "Error Image" window.
- Ideal improvements could involve using a more sophisticated error visualization technique, such as applying the `jet` color map from `matplotlib`.