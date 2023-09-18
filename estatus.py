import psutil as ps
import sys

def argumentos():
    if len(sys.argv)==1:
        print("no hay argumento")
        sys.exit(0)
    


def lock(target):
    for proc in ps.process_iter():
        if proc.name().lower()==target:
            proc.kill()
            print(f'{target} Detenido')
            
if __name__=="__main__":
    argumentos()
    target=sys.argv[1]
    
    while True:
        lock(target)