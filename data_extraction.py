import os
import git

# Clone the repository
repo_url = 'https://github.com/PhonePe/pulse.git'
clone_dir = 'phonepe_pulse_data'

def clone_repo():
    if not os.path.exists(clone_dir):
        git.Repo.clone_from(repo_url, clone_dir)
        print(f'Repository cloned to {clone_dir}')
    else:
        print(f'Repository already exists in {clone_dir}')

if __name__ == "__main__":
    clone_repo()