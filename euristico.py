from data_structure import *


def read_file_eur():
    in_file = open('first_adventure.in', 'r')
    num_providers, num_services, num_countries, num_projects = list(map(int, in_file.readline().split(' ')))
    # print(num_providers, num_services, num_countries, num_projects)
    services.append(in_file.readline().split(' ', num_services))
    # print(services)
    countries.append(in_file.readline().split(' ', num_countries))
    # print(countries)
    for _ in range(num_providers):
        provider_list = in_file.readline().split(' ')
        # print(provider_list)
        provider_name = provider_list[0]
        num_regions = int(provider_list[1])
        # print(num_regions)
        provider_temp = Provider(provider_name)
        for i in range(num_regions):
            region_name = in_file.readline()
            print(region_name)
            temp_shit = in_file.readline().split(' ')
            # print(temp_shit)
            package_number = int(temp_shit[0])
            # print(package_number)
            cost = float(temp_shit[1])
            # print(cost)
            service = list(map(int, temp_shit[2:-1]))
            # print(service)
            latency = list(map(int, in_file.readline().split(' ')[:-1]))
            # print(latency)
            region_temp = Region(region_name, package_number, cost, service, latency)
            provider_temp.add_region(region_temp)
            # print(len(providers))
        providers.append(provider_temp)
    # print(providers)
    # print(len(providers))
    for _ in range(num_projects):
        project_string = in_file.readline().split(' ')
        penalty = int(project_string[0])
        country = project_string[1]
        services_project = list(map(int, project_string[2:-1]))
        project_temp = Project(penalty, country, services_project)
        projects.append(project_temp)
        # print(project_string)
    # print(projects)
    # print(len(projects))
    in_file.close()


def eur_main():
    n = 50
    read_file_eur()
    o_file = open("output.txt", "w")
    num_proj = len(projects)
    for n_p, prov in enumerate(providers):
        for n_r, reg in enumerate(prov.region):
            #print(prov.name, reg.name)
            while reg.package_number > n:
                reg.package_number -= n
                o_file.write(str(n_p) + " " + str(n_r) + " " + str(n))
                num_proj -= 1
                if num_proj == 0:
                    o_file.write('\n')
                    o_file.close()
                    return
                print(reg.package_number)
                # if reg.package_number > 2*n:
                #    o_file.write(" ")
                o_file.write('\n')
    o_file.close()
    return


if __name__ == "__main__":
    eur_main()
