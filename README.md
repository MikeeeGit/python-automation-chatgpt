# python-automation-chatgpt

# Below is some stuff to add to bash to make it work chatgpt work from cmd line
# Lazygit
function lazygit() {
    git add .
    git commit -a -m "$1"
    git push
}
# Needed to make chatgpt work
export OPENAI_API_KEY=



# chatgpt cmd line
function chatgpt() {
    cd ~/python-automation-chatgpt
    python3 chatgpt.py "$1"
}

# pythoncode  -arg 1 is question, arg 2 is file name
function pythoncode() {
    cd ~/python-automation-chatgpt
    python3 python-chatgpt.py "$1" "$2"
}

# terraformcode - -arg 1 is question, arg 2 is file name
function terraformcode() {
    cd ~/python-automation-chatgpt
    python3 terraform-chatgpt.py "$1" "$2"
}

