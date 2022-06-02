import sys
import platform
import timeit
import os
import pycodestyle
import threading
from statistics import median
from multiprocessing import Pool
from concurrent.futures import ThreadPoolExecutor
from schematraportu import *

style_checker = pycodestyle.StyleGuide()
result = style_checker.check_files(['multithreading-multiprocessing.py'])

liczby = [15972490, 80247910, 92031257, 75940266,
          97986012, 87599664, 75231321, 11138524,
          68870499, 11872796, 79132533, 40649382,
          63886074, 53146293, 36914087, 62770938]


def obliczeniapool(x):
    suma = 0
    for i in range(1, x + 1):
        suma += ((x - i) * i)


def obliczeniathread():

    for number in liczby:
        suma = 0
        for i in range(1, number + 1):
            suma += ((number - i) * i)


def thread1():
    print('Wykonywanie obliczeń na jednym wątku.')
    t1 = threading.Thread(target=obliczeniathread)
    t1.start()
    t1.join()


def thread4():
    print('Wykonywanie obliczeń na czterech wątkach.')
    with ThreadPoolExecutor(max_workers=4) as executor:
        executor.map(obliczeniapool, liczby)


def pools4():
    print('Wykonywanie obliczeń na czterech procesach.')
    with Pool(4) as p1:
        p1.map(obliczeniapool, liczby)


def poolsmax():
    maxpool = os.cpu_count()
    print("Wykonywanie obliczeń na maksymalnej liczbie procesów, tj.:"
          + str(maxpool))
    with Pool(maxpool) as p2:
        p2.map(obliczeniapool, liczby)


def czas():
    tablica = []
    for i in range(1, 6):
        print("Cykl obliczeń nr: ", i, "z 5.")
        czasstart1 = timeit.default_timer()
        thread1()
        czasstop1 = timeit.default_timer()
        deltaczasu1 = czasstop1 - czasstart1
        print(f' {deltaczasu1:.3f}')

        czasstart2 = timeit.default_timer()
        thread4()
        czasstop2 = timeit.default_timer()
        deltaczasu2 = czasstop2 - czasstart2
        print(f' {deltaczasu2:.3f}')

        czasstart3 = timeit.default_timer()
        pools4()
        czasstop3 = timeit.default_timer()
        deltaczasu3 = czasstop3 - czasstart3
        print(f' {deltaczasu3:.3f}')

        czasstart4 = timeit.default_timer()
        poolsmax()
        czasstop4 = timeit.default_timer()
        deltaczasu4 = czasstop4 - czasstart4
        print(f' {deltaczasu4:.3f}')
        tablica.append(f' {deltaczasu1:.3f}')
        tablica.append(f' {deltaczasu2:.3f}')
        tablica.append(f' {deltaczasu3:.3f}')
        tablica.append(f' {deltaczasu4:.3f}')
    return tablica


def raport():
    listawynikow = list(czas())
    kolumna1 = (float(i) for i in listawynikow[0::4])
    kolumna2 = (float(i) for i in listawynikow[1::4])
    kolumna3 = (float(i) for i in listawynikow[2::4])
    kolumna4 = (float(i) for i in listawynikow[3::4])
    th1 = listawynikow[0]
    th2 = listawynikow[4]
    th3 = listawynikow[8]
    th4 = listawynikow[12]
    th5 = listawynikow[16]
    thm1 = listawynikow[1]
    thm2 = listawynikow[5]
    thm3 = listawynikow[9]
    thm4 = listawynikow[13]
    thm5 = listawynikow[17]
    proc1 = listawynikow[2]
    proc2 = listawynikow[6]
    proc3 = listawynikow[10]
    proc4 = listawynikow[14]
    proc5 = listawynikow[18]
    procm1 = listawynikow[3]
    procm2 = listawynikow[7]
    procm3 = listawynikow[11]
    procm4 = listawynikow[15]
    procm5 = listawynikow[19]

    fld1 = sorted(kolumna1)
    fld2 = sorted(kolumna2)
    fld3 = sorted(kolumna3)
    fld4 = sorted(kolumna4)

    med1 = median(fld1)
    med2 = median(fld2)
    med3 = median(fld3)
    med4 = median(fld4)

    # print(listawynikow)
    # print('1 wątek: ', kolumna1)
    # print('4 wątki: ', kolumna2)
    # print('4 procesy: ', kolumna3)
    # print('Unlimited power: ', kolumna4)

    wjp = str(platform.python_version())
    ni = str(platform.python_implementation())
    wi = str(sys.version)
    so = str(platform.system())
    wso = str(platform.release())
    proc = str(platform.processor())
    cores = str(os.cpu_count())
    print(wjp, ni, wi, so, wso, proc, cores)

    srodekraportu = "Wersja Pythona:" + wjp + "<br>Nazwa interpretera: " \
                    + ni + "<br>Wersja interpretera: " \
                    + wi + "<br>System operacyjny: " + so + \
                    "<br>Wersja systemu operacyjnego: " \
                    + wso + "<br>Rodzaj procesora: " + proc + \
                    "<br>Liczba rdzeni procesora: " \
                    + cores

    tabelka = (tr + td + "1" + ntd + td + str(th1) + ntd + td + str(thm1)
               + ntd + td + str(proc1) + ntd + td + str(procm1) + ntd + ntr +
               tr + td + "2" + ntd + td + str(th2) + ntd + td + str(thm2)
               + ntd + td + str(proc2) + ntd + td + str(procm2) + ntd + ntr +
               tr + td + "3" + ntd + td + str(th3) + ntd + td + str(thm3)
               + ntd + td + str(proc3) + ntd + td + str(procm3) + ntd + ntr +
               tr + td + "4" + ntd + td + str(th4) + ntd + td + str(thm4)
               + ntd + td + str(proc4) + ntd + td + str(procm4) + ntd + ntr +
               tr + td + "5" + ntd + td + str(th5) + ntd + td + str(thm5)
               + ntd + td + str(proc5) + ntd + td + str(procm5) + ntd + ntr
               + ntb)
    tabelka2 = (medianka + tr + td + 'Mediana:' + ntd + td + str(med1)
                + ntd + td + str(med2) + ntd + td + str(med3)
                + ntd + td + str(med4) + ntd + ntr + ntb)

    calyraport = (poczatekraportu + srodekraportu + naglowektabeli
                  + tabelka + tabelka2 + stopka)
    with open('report.html', 'w') as f:
        f.write(calyraport)


def main():
    raport()


if __name__ == '__main__':
    main()
    print(result.messages)
