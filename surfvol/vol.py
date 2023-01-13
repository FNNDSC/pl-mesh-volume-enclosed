from vtkmodules.vtkIOGeometry import vtkOBJReader
from pyvista import PolyData
from bicpl import PolygonObj
from bicpl.wavefront import WavefrontObj
from pathlib import Path
from tempfile import NamedTemporaryFile


def volume(mni_obj: Path) -> float:
    """
    Get the volume enclosed by a surface file.

    Supported formats: MNI .obj
    """
    surf = PolygonObj.from_file(mni_obj)
    wave = WavefrontObj.from_mni(surf)

    with NamedTemporaryFile('w', suffix='.obj') as f:
        wave.write_to(f)
        f.flush()
        poly_data = _read_wavefront_obj_as_vtk(f.name)

    return poly_data.volume


def _read_wavefront_obj_as_vtk(file_name: str) -> PolyData:
    reader = vtkOBJReader()
    reader.SetFileName(file_name)
    reader.Update()
    obj = reader.GetOutput()
    return PolyData(obj)
