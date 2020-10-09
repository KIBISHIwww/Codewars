#   Write a function that when given a URL as a string, parses out just the domain name and returns it as a string.
#   For example:
#       domain_name("http://github.com/carbonfive/raygun") == "github" 
#       domain_name("http://www.zombie-bites.com") == "zombie-bites"
#       domain_name("https://www.cnet.com") == "cnet"

def domain_name(url):
    import re
    return re.search('(https://)?(www\d?\.)?(?P<domain>[\w-]+)\.', url).group('domain')

#   Also can use split() to solve the problem
def domain_name(url):
    return url.split("//")[-1].split("www.")[-1].split(".")[0]  #[-1] means the last item
