import routines

blob_ressources = {}

def init_blob_ressources():
    if blob_ressources == {}:
        blob_ressources['left_blob1'] = routines.load_png('pnj/enemy/blob/left_blob1.png')
        blob_ressources['left_blob2'] =  routines.load_png('pnj/enemy/blob/left_blob2.png')
        blob_ressources['left_blob3'] =  routines.load_png('pnj/enemy/blob/left_blob3.png')
        blob_ressources['left_blob4'] =  routines.load_png('pnj/enemy/blob/left_blob4.png')
        blob_ressources['left_blob5'] =  routines.load_png('pnj/enemy/blob/left_blob5.png')
        blob_ressources['left_blob6'] =  routines.load_png('pnj/enemy/blob/left_blob6.png')
        blob_ressources['right_blob1'] =  routines.load_png('pnj/enemy/blob/right_blob1.png')
        blob_ressources['right_blob2'] =  routines.load_png('pnj/enemy/blob/right_blob2.png')
        blob_ressources['right_blob3'] =  routines.load_png('pnj/enemy/blob/right_blob3.png')
        blob_ressources['right_blob4'] =  routines.load_png('pnj/enemy/blob/right_blob4.png')
        blob_ressources['right_blob5'] =  routines.load_png('pnj/enemy/blob/right_blob5.png')
        blob_ressources['right_blob6'] =  routines.load_png('pnj/enemy/blob/right_blob6.png')
