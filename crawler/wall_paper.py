# -*- coding:utf-8 -*-

from requests import get
from filetype import guess
from os import rename
from os import makedirs
from os.path import exists
from json import loads
from contextlib import closing

mock_user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) " \
                  "Chrome/63.0.3239.132 Safari/537.36 "
user_agent_header = "User-Agent"
content_length_header = 'content-length'
headers = {user_agent_header: mock_user_agent}
type_dict = {1: "latest", 2: "hottest", 3: "girls", 4: "stars"}


# file download
def download(download_url, file_full_name, now_photo_count, all_photo_count):

    # download pictures
    with closing(get(download_url, headers=headers, stream=True)) as response:
        # single request max chunk size
        chunk_size = 1024
        # get content length of file in response
        content_size = int(response.headers[content_length_header])
        # calculate the process of download
        data_count = 0
        with open(file_full_name, "wb") as file:
            for data in response.iter_content(chunk_size=chunk_size):
                # write data to the file
                file.write(data)
                # calculate the process block
                done_block = int((data_count / content_size) * 50)
                data_count = data_count + len(data)
                # calculate the percentage pf process
                now_jd = (data_count / content_size) * 100
                print("\r %s：[%s%s] %d%% %d/%d" % (
                    file_full_name, done_block * '█', ' ' * (50 - 1 - done_block), now_jd, now_photo_count,
                    all_photo_count), end=" ")

    # get the file type
    file_type = guess(file_full_name)
    # rename the file (add the file type extension)
    rename(file_full_name, file_full_name + '.' + file_type.extension)


# 爬取不同类型图片
def crawler_photo(type_id, photo_count):
    url_api = "https://service.paper.meiyuan.in/api/v2/columns/flow/"
    photo_type_guid_dict = {type_dict.get(1): "5c68ffb9463b7fbfe72b0db0",
                            type_dict.get(2): "5c69251c9b1c011c41bb97be",
                            type_dict.get(3): "5c81087e6aee28c541eefc26",
                            type_dict.get(4): "5c81f64c96fad8fe211f5367"}
    query_param_start_symbol = "?"
    query_param_equal_symbol = "="
    query_param_and_symbol = "&"
    query_param_dict = {"page": 1, "per_page": photo_count}

    query_param_list = []
    for key, value in query_param_dict.items():
        query_param_list.append(str(key + query_param_equal_symbol + str(value)))
    query_param_str = query_param_and_symbol.join(query_param_list)

    # latest 1, hottest 2, girls 3, stars 4
    photo_type_guid = photo_type_guid_dict.get(type_dict.get(type_id))

    url = url_api + photo_type_guid + query_param_start_symbol + query_param_str

    # Get the response of api
    respond = get(url, headers=headers)
    # Convert the response to object
    photo_data = loads(respond.content)

    # counter for photos which has been downloaded
    now_photo_count = 1

    # the amount of all photos
    all_photo_count = len(photo_data)

    # start to download and save
    for photo in photo_data:

        # create directory to save
        if not exists('./' + str(type_dict.get(type_id))):
            makedirs('./' + str(type_dict.get(type_id)))

        # get the url of photos
        file_url = photo['urls']['raw']

        # get the file name
        file_name_only = file_url.split('/')
        file_name_only = file_name_only[len(file_name_only) - 1]

        # rename the file
        file_full_name = './' + type_dict.get(type_id) + '/' + file_name_only

        # start to download the photo
        download(file_url, file_full_name, now_photo_count, all_photo_count)
        now_photo_count = now_photo_count + 1


if __name__ == '__main__':

    # Latest 1, Hottest 2, Girls 3, Stars 4
    wall_paper_id = 1
    wall_paper_count = 10
    while True:

        print('\n\n')

        # Choose type of wall paper
        wall_paper_id = input("Wallpaper Type：Latest 1, Hottest 2, Girls 3, Stars 4\nPlease input number to choose "
                              "type：")
        # Validate the input
        while (wall_paper_id != str(1) and wall_paper_id != str(2) and wall_paper_id != str(3) and wall_paper_id != str(
                4)):
            print('Please validate your input!\n')
            wall_paper_id = input("Wallpaper Type：Latest 1, Hottest 2, Girls 3, Stars 4\nPlease input number to choose "
                                  "type：")
        # Input the amount of wall papers
        wall_paper_count = input("Please input the amount of pictures：")
        # Validate the input
        while int(wall_paper_count) <= 0:
            print("Please validate your input!\n")
            wall_paper_count = input("Please input the amount of pictures：")

        # Start to download
        print("Downloading the picture, please wait...")
        crawler_photo(int(wall_paper_id), int(wall_paper_count))
        print('\nDownload Success!')

        if_continue = input("Continue(Y/N)?:")
        while str(if_continue).upper() != 'Y' and str(if_continue).upper() != 'N':
            if_continue = input("Continue(Y/N)?:")
        if 'N' == str(if_continue).upper():
            break
