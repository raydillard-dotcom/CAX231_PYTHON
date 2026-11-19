
def main():
    print(" GPS Coordinates Tracker \n")
    
    #Store latitude and longitude inside a single tuple named destination
    destination = (34.0522, -118.2437)
    print(f"Destination:: {destination}")
    
    #Print out the latitude by accessing index 0 of the tuple
    print("\n--- Method A: Index Access ---")
    print(f"Latitude (accessed via index 0): {destination[0]}")
    print(f"Longitude (accessed via index 1): {destination[1]}")
    
    #Unpack the tuple directly into two new variables named latitude and longitude
    print("\n--- Method B: Tuple Unpacking ---")
    latitude, longitude = destination
    
    print(f"Unpacked latitude variable: {latitude}")
    print(f"Unpacked longitude variable: {longitude}")

if __name__ == "__main__":
    main()
