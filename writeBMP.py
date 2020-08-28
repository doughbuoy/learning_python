"""A module that creates BMP bitmap Image Files"""

def write_greyscale(FQN,PIXELS):
    """Creates a BMP FILE"""
    HEIGHT = len(PIXELS)
    WIDTH = len(PIXELS[0])

    with open(FQN,mode='wb') as BMPOUT:
        #Write the Binary Header
        BMPOUT.write(b'BM')

        SIZE_BOOKMARK = BMPOUT.tell()                # next 4 bytes hold the filesize as 32 bit
        BMPOUT.write(b'\x00\x00\x00\x00')
        BMPOUT.write(b'\x00\x00')                   # UNUSED 16 bit
        BMPOUT.write(b'\x00\x00')                   # UNUSED 16 bit

        PIXEL_OFFSET_BOOKMARK = BMPOUT.tell()       # Next 4 bytes hold the int offset to the
        BMPOUT.write(b'\x00\x00\x00\x00')           #PIXEL Data .... zero for now
        # IMAGE HEADER
        BMPOUT.write(b'\x28\x00\x00\x00')           # image size in bytes (40 Decimal)
        BMPOUT.write(_INT32_to_bytes(WIDTH))        #Image Width n pixels
        BMPOUT.write(_INT32_to_bytes(HEIGHT))       # Image HEIGHT in pixels
        BMPOUT.write(b'\x01\x00')                   # Numb of Image Planes
        BMPOUT.write(b'\x08\x00')                   # bits per pixel (8)
        BMPOUT.write(b'\x00\x00\x00\x00')           # No Compression
        BMPOUT.write(b'\x00\x00\x00\x00')           # Zero for uncompressed Image
        BMPOUT.write(b'\x00\x00\x00\x00')           # Unused Pixel Meter
        BMPOUT.write(b'\x00\x00\x00\x00')           # Use Whole Color Table
        BMPOUT.write(b'\x00\x00\x00\x00')           # All colours are important

        #  Color pallet
        for c in range(256):
            BMPOUT.write(bytes((c, c, c, 0)))       # Blue, Green, Red, Zero

        # PIXEL DATA
        PIXEL_DATA_BOOKMARK =  BMPOUT.tell()        # Another File Bookmark
        for ROW in reversed(PIXELS):                # BMP Files are bottom to top
            ROW_DATA = bytes(ROW)
            BMPOUT.write(ROW_DATA)
            PADDING = b'\x00' * ((4 - (len(ROW) % 4)) % 4)
            BMPOUT.write(PADDING)

        # EOF MARK
        EOF_BOOKMARK = BMPOUT.tell()

        #Fill in file Size
        BMPOUT.seek(SIZE_BOOKMARK)

        BMPOUT.write(_int32_to_bytes(EOF_BOOKMARK)

        # fill in pixel offset
        BMPOUT.seek(PIXEL_OFFSET_BOOKMARK)
        BMPOUT.write(_int_to_bytes(PIXEL_DATA_BOOKMARK))






