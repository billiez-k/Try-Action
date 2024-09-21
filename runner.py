import subprocess
import time

def commit_changes():
    subprocess.run(["git", "add", "."], check=True)
    subprocess.run(["git", "commit", "-m", "Auto-commit after successful autoblogger iteration"], check=True)
    subprocess.run(["git", "push"], check=True)

def autoblogger(a, b):
    with open(f"{a}.txt", "w") as f:
      f.write(a)
      f.write("\n")
      f.write(str(b))
      time.sleep(60)
    commit_changes()

def main():
    queries = ["香港人愛吃台灣的什麼",
"哪種食物最能代表香港的飲食",
"最能代表香港的食物",
"香港自由行吃什麼",
"香港宵夜去哪吃",
"香港為什麼是美食天堂",
"香港飲食文化多元化的原因",
"茶餐廳是香港本土文化的代表嗎",
"為什麼茶餐廳是研究香港文化的好地方",
"香港的飲食文化如何融合中國和西方國家的特色",
"粵菜跟港式一樣嗎",
"去香港一定要吃什麼",
"香港人喜歡吃什麼菜",
"香港人早餐喜歡吃什麼"]
    categories = [['美食', '台灣美食'], ['美食', '香港'], ['美食', '香港'], ['美食', '香港'], ['美食', '香港'], ['美食', '香港'], ['美食', '香港'], ['美食', '香港'], ['美食', '香港'], ['美食', '香港'], ['美食', '香港'], ['美食', '香港'], ['美食', '香港'], ['美食', '香港']]
    model = "meta/llama-3.1-405b-instruct"
    size = 4
    sample_size = 4
    lang = "traditional chinese"
    outline_editor = False
    for query, category in zip(queries, categories):
        autoblogger(query, category)

if __name__ == "__main__":
    main()
