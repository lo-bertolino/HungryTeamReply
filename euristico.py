from data_structure import *


def read_file():
    in_file = open('first_adventure.in', 'r')
    num_providers, num_services, num_countries, num_projects = list(map(int, in_file.readline().split(' ')))
    print(num_providers, num_services, num_countries, num_projects)
    services.append(in_file.readline().split(' ', num_services))
    print(services)
    countries.append(in_file.readline().split(' ', num_countries))
    print(countries)
    for _ in range(num_providers):
        provider_list = in_file.readline().split(' ')
        print(provider_list)
        provider_name = provider_list[0]
        num_regions = int(provider_list[1])
        provider_temp = Provider(provider_name)
        for _ in range(num_regions):
            region_name = in_file.read()
            print(region_name)
            temp_shit = in_file.read()
            print(temp_shit)
            package_number = int(temp_shit)
            print(package_number)
            cost = float(in_file.read())
            print(cost)
            service = list(map(int, in_file.readline().split(' ')))
            print(service)
            latency = list(map(int, in_file.readline().split(' ')))
            print(latency)
            region_temp = Region(region_name, package_number, cost, service, latency)
            provider_temp.add_region(region_temp)
            print(len(providers))
        providers.append(provider_temp)
    print(providers)
    print(len(providers))
    for _ in range(num_projects):
        penalty = int(in_file.read())
        country = in_file.read()
        services_project = list(map(int, in_file.readline().split(' ')))
        project_temp = Project(penalty, country, services_project)
        projects.append(project_temp)
    print(projects)
    print(len(projects))
    in_file.close()


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
                num_proj -= 1
                if num_proj == 0:
                    o_file.write('\n')
                    return
                # if reg.package_number > 2*n:
                #    o_file.write(" ")
            o_file.write('\n')

    return


if __name__ == "__main__":
    eur_main()
