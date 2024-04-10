from pyclass import axiclass

from .cosmology import BaseEngine
from . import classy


class AxiClassEngine(classy.ClassEngine):

    """Engine for the Boltzmann code AxiCLASS."""

    name = 'axiclass'
    
#     def __init__(self, *args, **kwargs):
#         super(classy.ClassEngine).__init__(*args, **kwargs)
#         params['n_axion'] = params['n_axion']

    def _set_classy(self, params):

        class _ClassEngine(axiclass.ClassEngine):
            
            

            def compute(self, tasks):
                try:
                    return super(_ClassEngine, self).compute(tasks)
                except axiclass.ClassInputError as exc:
                    raise CosmologyInputError from exc
                except axiclass.ClassComputationError as exc:
                    raise CosmologyComputationError from exc

        self.classy = _ClassEngine(params=params)


class Background(classy.BaseClassBackground, axiclass.Background):

    """Your modifications, if any."""


class Primordial(classy.BaseClassPrimordial, axiclass.Primordial):
    
     """Your modifications, if any."""
    
class Perturbations(classy.BaseClassPerturbations, axiclass.Perturbations):
    
     """Your modifications, if any."""
        
    
class Transfer(classy.BaseClassTransfer, axiclass.Transfer):
    
     """Your modifications, if any."""
        
class Harmonic(classy.BaseClassHarmonic, axiclass.Harmonic):
     """Your modifications, if any."""
        
    
class Fourier(classy.BaseClassFourier, axiclass.Fourier):
     """Your modifications, if any."""