from multiprocessing import Process
import os, sys, mmap


def function_hijo(content, mem):
    mem.write(content)
    mem.flush()


file_size = 100
mem = mmap.mmap(-1, file_size)
content = sys.argv[1].encode()

p = Process(target=function_hijo, args=(content, mem))
p.start()
p.join()

mem.seek(0)
print("Contenido en memoria: " + mem.read().decode())
mem.close()
