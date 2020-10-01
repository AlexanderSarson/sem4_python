from concurrent.futures import ThreadPoolExecutor
import webget


# def get_img_urls():
#     my_dict = dict()
#     for height in range(100, 600, 200):
#         for width in range(100, 600, 200):
#             for background in range(0, 16, 2):
#                 for foreground in range(0, 16, 2):
#                     my_dict[f"img{width}x{height}-{background:x}{background:x}{background:x}-{foreground:x}{foreground:x}{foreground:x}.png"] = f"https://dummyimage.com/{width}x{height}/{background:x}{background:x}{background:x}/{foreground:x}{foreground:x}{foreground:x}"
#     return my_dict

def get_img_urls():
    urls, filenames = [], []
    for height in range(100, 600, 200):
        for width in range(100, 600, 200):
            for background in range(0, 16, 2):
                for foreground in range(0, 16, 2):
                    # print('{:X}'.format(i)*3)
                    urls.append('https://dummyimage.com/{width}x{height}/{background:x}{background:x}{background:x}/{foreground:x}{foreground:x}{foreground:x}'
                                .format(height=height, width=width, background=background, foreground=foreground))
                    filenames.append('img{width}x{height}-{background:x}{background:x}{background:x}-{foreground:x}{foreground:x}{foreground:x}.png'
                                     .format(height=height, width=width, background=background, foreground=foreground))
    return urls, filenames


# def download_urls(urls):
#     for idx, url in enumerate(urls):
#         webget.download(url, to=f'todelete/{idx}.png')

def download_urls(urls, filenames):
    for idx, url in enumerate(urls):
        webget.download(url, to=f'todelete/{filenames[idx]}')


def multithreading():
    args = ((url, filename) for (url, filename) in get_img_urls())
    with ThreadPoolExecutor(4) as ex:
        res = ex.map(download_urls, args)
    return list(res)


multithreading()
