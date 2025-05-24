from data.analysis import load_data
from streamlit.delta_generator import DeltaGenerator

def Culture(main:DeltaGenerator) -> None:
    datasets = load_data()
    main.header("Datasets")
    for name, data  in zip(datasets.keys(), datasets.values()):
        main.write(name)
        main.dataframe(data)
        main.divider()
