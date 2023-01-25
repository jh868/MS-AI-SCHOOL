from torch.utils.data import Dataset
import os
import glob
import torch
import cv2


class customDataset(Dataset):
    def __init__(self, path, transform=None):
        self.all_image_path = glob.glob(os.path.join(path, '*', '*.jpg'))
        self.transform = transform
        self.label_dict = {'african-wildcat': 0,
                           'blackfoot-cat': 1,
                           'chinese-mountain-cat': 2,
                           'domestic-cat': 3,
                           'european-wildcat': 4,
                           'jungle-cat': 5,
                           'sand-cat': 5
                           }

    def __getitem__(self, item):
        img_path = self.all_image_path[item]
        # label
        folder_name = img_path.split('/')[3]
        label = self.label_dict[folder_name]

        # image
        img = cv2.imread(img_path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # Augment
        if self.transform is not None:
            img = self.transform(image=img)['image']

        # print(img, label)
        return img, label

    def __len__(self):
        return len(self.all_image_path)


# if __name__ == '__main__':
#     test = customDataset('./dataset/train', transform=None)
#     for i in test:
#         pass
