from srModule import song
import time
#song0 = song.initFromFile("/Users/luyijou/Desktop/ Mine/Python/SongRecogn/songp/liangyu_01.mp3")
song0 = song.initFromFile("song/yinghuazhanfangshi.mp3")
print(song0.getId())
print("get")
print(song0.fs,song0.channels)
print(len(song0.getFingerprint()))
print("down")
song0.insertFingerprints()
print("ok")
# a = time.time()
# print(song0.recognize())
# b = time.time()
# print(b-a)