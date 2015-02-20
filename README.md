# tracker

# Get Video Input 
    # Use a webcam to get video input
    # PIL to take screen shots every interval
    
# recognize what we are tracking/track
    # use an orange sticker on a stick
    # phase 1: orange sticker discover
        # scan whole image until you find the orange sticker
        # once found, save the position
        # define a bounding box around the sticker to do future searches
    # phase 2: orange sticker follow
        # scan bounding box to find new position of sticker
        # redefine bounding box centered at new sticker position
        # if orange sticker is not found, go back to phase 1

# output motion
    # save the orange sticker positions and draw pointwise