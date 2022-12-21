# NectoT, Saitama12-afro1, Vivarlee, The-Vlad
# Напишите функцию main, в которую подаётся двумерный массив terrain, сила гравитации g (клетка в секунду) и время n (в секундах).
# terrain представляет из себя карту (земля в разрезе, как в террарии, хз как лучше объяснить),
# где 0 обозначает воздух, 1 - землю, а 2 - воду.
# Напишите максимально правдоподобную физику воды и верните обновлённый массив terrain после симуляции физики воды на протияжении n секунд 
# (То есть обновлённый terrain по прошествию n секунд).
# Реалистичность алгоритма будет оценена по десятибальной шкале человеком, не участвовавшим в написании кода.
def main(terrain:list[list[int]], g: int, n: int) -> list[list[int]]:
    for i in range(len(terrain)):
        current_level = terrain[i]
        for pixel in range(len(current_level)):
            if current_level[pixel] == 2:
                buff = i + 1
                while True:
                    if terrain[buff][pixel] == 0:
                        current_level[pixel], terrain[buff][pixel] = 0, 2
                    else: break
