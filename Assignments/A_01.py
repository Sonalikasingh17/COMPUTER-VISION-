'''
Load an image from a user-specified location,
convert it to grayscale,
and either display it or save it based on user input.

'''



import cv2

# Ask user for image location
img_path = input("Enter the location of the image: ")

# Load the image
img = cv2.imread(img_path)

# Check if image loaded successfully
if img is None:
    print("Error: Image not found or invalid path!")
    exit()

# Convert to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Ask user whether to display or save
choice = input("Do you want to display or save the image? (display/save): ").strip().lower()

if choice == "display":
    cv2.imshow("Grayscale Image", gray_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

elif choice == "save":
    output_name = input("Enter output file name (e.g., output.jpg): ")
    cv2.imwrite(output_name, gray_img)
    print("Image saved successfully as:", output_name)

else:
    print("Invalid option. Please choose either 'display' or 'save'.")
