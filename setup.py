import setuptools


# Set the torchaudio version based on the PyTorch version
def get_torchaudio_version():
    import torch
    torch_version = torch.__version__
    print("========================================")
    print("pytorch_version", torch_version)
    print("========================================")
    if torch_version.startswith("1.13"):
        return "torchaudio==0.13.1"
    elif torch_version.startswith("1.12"):
        return "torchaudio==0.12.1"
    elif torch_version.startswith("1.11"):
        return "torchaudio==0.11.0"
    elif torch_version.startswith("1.10"):
        return "torchaudio==0.10.0"
    elif torch_version.startswith("1.9"):
        return "torchaudio==0.9.1"
    elif torch_version.startswith("1.8"):
        return "torchaudio==0.8.1"
    elif torch_version.startswith("1.7"):
        return "torchaudio==0.7.2"
    elif torch_version.startswith("1.6"):
        return "torchaudio==0.6.0"
    elif torch_version.startswith("1.5"):
        return "torchaudio==0.5.0"
    elif torch_version.startswith("1.4"):
        return "torchaudio==0.4.0"
    else:
        raise ValueError("Unsupported PyTorch version")


# Install torchaudio
setuptools.setup(
    name="bindtorchaudio",
    version="0.3",
    install_requires=[
        get_torchaudio_version()
    ]
)
