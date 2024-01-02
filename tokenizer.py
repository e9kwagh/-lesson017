"""new"""
import requests


# def tokenizer(target, prefix, suffix):
#     a = requests.get(target)
#     return list_of_tokens_that_match


def tokenizer(target, prefix, suffix):
    """tokenizer"""
    list_of_tokens_that_match = []
    for i in target:
        if prefix in i and suffix in i :
            start= i[i.index(prefix): ]
            end = start[:start.index(suffix)]
            list_of_tokens_that_match.append(end)

    return list_of_tokens_that_match

def get_url_list(url):
    """get_url_list"""
    data = requests.get(url,timeout=10)
    li = data.text.split("\n")
    webpage_source = [i for i in li if "href" in i ]
    url_list = tokenizer(webpage_source, "http",'"')

    return url_list

def infix_to_postfix(infix_expression: str):
    """this is the postfix to prefix"""

    power= {
        '^' :3,
        '*' :2,
        '/' :2,
        '+' :1,
        '-' :1
    }
    prefixer = ""
    stack = []
    operators = ["^","*","/","+","-",")","("]
    # charter =["a","b","c","d","q"]

    for char in infix_expression :
        if char not in operators :
            prefixer += char
        elif char == "(" :
            stack.append("(")
        elif char == ")" :
            while stack and stack[len(stack)-1] != "(" :
                val = stack.pop()
                prefixer += val
            stack.pop()
        else :
            while stack and stack[len(stack)-1] != "(" and power[char] <= power[stack[len(stack)-1]] :
                d_val = stack.pop()
                prefixer += d_val
            stack.append(char)

    while stack:
        f_val = stack.pop()
        prefixer += f_val
    return prefixer

if __name__ in "__main__":
    # print(get_url_list("https://httpbin.org"))
    print(infix_to_postfix("(a+b)^c-d/q"))
