from storage_manager import StorageManager
import os


sm = StorageManager()

def send_images_example():
    public_urls = []
    #get the list of file store in the vid1 and vid2 directories
    vid1= os.listdir('images/vid1')
    vid2 = os.listdir('images/vid2')

    for i in range(len(vid1)):
        public_url1 = sm.upload_file(file_name=f'tennis/{vid1[i]}', local_path=f'images/vid1/{vid1[i]}')
        public_url2 = sm.upload_file(file_name=f'tennis/{vid2[i]}', local_path=f'images/vid2/{vid2[i]}')
        public_urls.append((public_url1,public_url2))
    return public_urls

# print(send_images_example())
