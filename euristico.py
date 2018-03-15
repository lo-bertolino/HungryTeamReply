from data_structure import *


def read_file():
    path = 'first_adventure.in'
    i_file = open(path, 'r')
    num_providers, num_services, num_countries, num_projects = list(map(int, i_file.readline().split(' ')))
    services.append(i_file.readline().split(' '))
    countries.append(i_file.readline().split(' '))
    for _ in range(num_providers):
        provider_list = i_file.readline().split(' ')
        provider_name = provider_list[0]
        num_regions = int(provider_list[1])
        provider_temp = Provider(provider_name)
        for _ in range(num_regions):
            region_name = i_file.read()
            package_number = int(i_file.read())
            cost = float(i_file.read())
            service = list(map(int, i_file.readline().split(' ')))
            latency = list(map(int, i_file.readline().split(' ')))
            region_temp = Region(region_name, package_number, cost, service, latency)
            provider_temp.add_region(region_temp)

        providers.append(provider_temp)

    for _ in range(num_projects):
        penalty = int(i_file.read())
        country = i_file.read()
        services_project = list(map(int, i_file.readline().split(' ')))
        project_temp = Project(penalty, country, services_project)
        projects.append(project_temp)


def eur_main():
    n = 50
    read_file()
    o_file = open("output.txt", "w")
    cur_prov = 0
    cur_reg = 0
    num_proj = len(projects)
    for n_p, prov in enumerate(providers):
        for n_r, reg in enumerate(prov.region):
            while reg.package_number > n:
                reg.package_number -= n
                o_file.write(str(n_p) + " " + str(n_r) + " " + n)
                num_proj-=1
                if num_proj == 0:
                    o_file.write('\n')
                    return
                # if reg.package_number > 2*n:
                #    o_file.write(" ")
            o_file.write('\n')

    return


if __name__ == "__main__":
    eur_main()
