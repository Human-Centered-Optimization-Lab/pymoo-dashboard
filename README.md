# pymoo dashboard

_A tool to display live visualizations of your pymoo projects in real time_

## Development Setup

### Python requirements
You will need to install Python (and preferably Anaconda). Once your environment is set up, you will need to run:

```shell
pip install -r requirements.txt 
```

### Node requirements
This project uses Node, Nuxt, and Vue to build its front end UI. So to start: 
1. Install Node.js
2. Enter the front end directory `cd frontend`
3. Run `npm install`

### Linting Requirements
This project uses ESLint to lint the front end code. If you are using VSCode, you can install the [ESLint extension](https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint) to get linting in real time.

## Running for development

The following command will run a sample optimization problem.
```
python Dashboard.py
```


## Building the project
For Unix based OSes
```
./build.sh
```


## Deploying to pymoo

Simply set the Pymoo callback function as `Dashboard()` and you're good to go. 
Make sure the `Dashboard.html`, `Dashboard.js`, and `Dashboard.css` are all in the 
same directory as whereever `Dashboard.py` is deployed to.

## Example: 
```python         
    # create the reference directions to be used for the optimization
    ref_dirs = get_reference_directions("das-dennis", 3, n_partitions=12)

    # create the algorithm object
    algorithm = NSGA3(pop_size=92,
                      ref_dirs=ref_dirs)

    # execute the optimization
    res = minimize(get_problem("dtlz1"),
                   algorithm,
                   seed=2018194,
                   callback=Dashboard(),
                   termination=('n_gen', 600))
```

