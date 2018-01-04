# DO NOT MODIFY THIS FILE DIRECTLY.  THIS FILE MUST BE CREATED BY
# mf6/utils/createpackages.py
from .. import mfpackage
from ..data.mfdatautil import ListTemplateGenerator, ArrayTemplateGenerator


class ModflowGwfdisu(mfpackage.MFPackage):
    """
    ModflowGwfdisu defines a disu package within a gwf6 model.

    Parameters
    ----------
    length_units : string
        * length_units (string) is the length units used for this model. Values
          can be "FEET", "METERS", or "CENTIMETERS". If not specified, the
          default is "UNKNOWN".
    nogrb : boolean
        * nogrb (boolean) keyword to deactivate writing of the binary grid
          file.
    xorigin : double
        * xorigin (double) x-position of the origin used for model grid
          vertices. This value should be provided in a real-world coordinate
          system. A default value of zero is assigned if not specified. The
          value for texttt{xorigin} does not affect the model simulation, but
          it is written to the binary grid file so that postprocessors can
          locate the grid in space.
    yorigin : double
        * yorigin (double) y-position of the origin used for model grid
          vertices. This value should be provided in a real-world coordinate
          system. If not specified, then a default value equal to zero is used.
          The value for texttt{yorigin} does not affect the model simulation,
          but it is written to the binary grid file so that postprocessors can
          locate the grid in space.
    angrot : double
        * angrot (double) counter-clockwise rotation angle (in degrees) of the
          model grid coordinate system relative to a real-world coordinate
          system. If not specified, then a default value of 0.0 is assigned.
          The value for texttt{angrot} does not affect the model simulation,
          but it is written to the binary grid file so that postprocessors can
          locate the grid in space.
    nodes : integer
        * nodes (integer) is the number of cells in the model grid.
    nja : integer
        * nja (integer) is the sum of the number of connections and
          texttt{nodes}. When calculating the total number of connections, the
          connection between cell :math:`n` and cell :math:`m` is considered to
          be different from the connection between cell :math:`m` and cell
          :math:`n`. Thus, texttt{nja} is equal to the total number of
          connections, including :math:`n` to :math:`m` and :math:`m` to
          :math:`n`, and the total number of cells.
    nvert : integer
        * nvert (integer) is the total number of (x, y) vertex pairs used to
          define the plan-view shape of each cell in the model grid. If
          texttt{nvert} is not specified or is specified as zero, then the
          VERTICES and CELL2D blocks below are not read.
    top : [double]
        * top (double) is the top elevation for each cell in the model grid.
    bot : [double]
        * bot (double) is the bottom elevation for each cell.
    area : [double]
        * area (double) is the cell surface area (in plan view).
    iac : [integer]
        * iac (integer) is the number of connections (plus 1) for each cell.
          The sum of texttt{iac} must be equal to texttt{nja}.
    ja : [integer]
        * ja (integer) is a list of cell number (n) followed by its connecting
          cell numbers (m) for each of the m cells connected to cell n. The
          number of values to provide for cell n is texttt{iac(n)}. This list
          is sequentially provided for the first to the last cell. The first
          value in the list must be cell n itself, and the remaining cells must
          be listed in an increasing order (sorted from lowest number to
          highest). Note that the cell and its connections are only supplied
          for the GWF cells and their connections to the other GWF cells. Also
          note that the JA list input may be chopped up to have every node
          number and its connectivity list on a separate line for ease in
          readability of the file. To further ease readability of the file, the
          node number of the cell whose connectivity is subsequently listed,
          may be expressed as a negative number the sign of which is
          subsequently corrected by the code.
    ihc : [integer]
        * ihc (integer) is an index array indicating the direction between node
          n and all of its m connections. If :math:`ihc=0` -- cell :math:`n`
          and cell :math:`m` are connected in the vertical direction. Cell
          :math:`n` overlies cell :math:`m` if the cell number for :math:`n` is
          less than :math:`m`; cell :math:`m` overlies cell :math:`n` if the
          cell number for :math:`m` is less than :math:`n`. If :math:`ihc=1` --
          cell :math:`n` and cell :math:`m` are connected in the horizontal
          direction. If :math:`ihc=2` -- cell :math:`n` and cell :math:`m` are
          connected in the horizontal direction, and the connection is
          vertically staggered. A vertically staggered connection is one in
          which a cell is horizontally connected to more than one cell in a
          horizontal connection.
    cl12 : [double]
        * cl12 (double) is the array containing connection lengths between the
          center of cell :math:`n` and the shared face with each adjacent
          :math:`m` cell.
    hwva : [double]
        * hwva (double) is a symmetric array of size texttt{nja}. For
          horizontal connections, entries in texttt{hwva} are the horizontal
          width perpendicular to flow. For vertical connections, entries in
          texttt{hwva} are the vertical area for flow. Thus, values in the
          texttt{hwva} array contain dimensions of both length and area.
          Entries in the texttt{hwva} array have a one-to-one correspondence
          with the connections specified in the texttt{ja} array. Likewise,
          there is a one-to-one correspondence between entries in the
          texttt{hwva} array and entries in the texttt{ihc} array, which
          specifies the connection type (horizontal or vertical). Entries in
          the texttt{hwva} array must be symmetric; the program will terminate
          with an error if the value for texttt{hwva} for an :math:`n-m`
          connection does not equal the value for texttt{hwva} for the
          corresponding :math:`m-n` connection.
    angldegx : [double]
        * angldegx (double) is the angle (in degrees) between the horizontal
          x-axis and the outward normal to the face between a cell and its
          connecting cells (see figure 8 in the MODFLOW-USG documentation). The
          angle varies between zero and 360.0 degrees. texttt{angldegx} is only
          needed if horizontal anisotropy is specified in the NPF Package or if
          the XT3D option is used in the NPF Package. texttt{angldegx} does not
          need to be specified if horizontal anisotropy or the XT3D option is
          not used. texttt{angldegx} is of size nja; values specified for
          vertical connections and for the diagonal position are not used. Note
          that texttt{angldegx} is read in degrees, which is different from
          MODFLOW-USG, which reads a similar variable (anglex) in radians.
    verticesrecarray : [iv, xv, yv]
        * iv (integer) is the vertex number. Records in the VERTICES block must
          be listed in consecutive order from 1 to texttt{nvert}.
        * xv (double) is the x-coordinate for the vertex.
        * yv (double) is the y-coordinate for the vertex.
    cell2drecarray : [icell2d, xc, yc, ncvert, icvert]
        * icell2d (integer) is the cell2d number. Records in the CELL2D block
          must be listed in consecutive order from 1 to texttt{nodes}.
        * xc (double) is the x-coordinate for the cell center.
        * yc (double) is the y-coordinate for the cell center.
        * ncvert (integer) is the number of vertices required to define the
          cell. There may be a different number of vertices for each cell.
        * icvert (integer) is an array of integer values containing vertex
          numbers (in the VERTICES block) used to define the cell. Vertices
          must be listed in clockwise order.

    """
    top = ArrayTemplateGenerator(('gwf6', 'disu', 'griddata', 'top'))
    bot = ArrayTemplateGenerator(('gwf6', 'disu', 'griddata', 'bot'))
    area = ArrayTemplateGenerator(('gwf6', 'disu', 'griddata', 'area'))
    iac = ArrayTemplateGenerator(('gwf6', 'disu', 'connectiondata', 
                                  'iac'))
    ja = ArrayTemplateGenerator(('gwf6', 'disu', 'connectiondata', 
                                 'ja'))
    ihc = ArrayTemplateGenerator(('gwf6', 'disu', 'connectiondata', 
                                  'ihc'))
    cl12 = ArrayTemplateGenerator(('gwf6', 'disu', 'connectiondata', 
                                   'cl12'))
    hwva = ArrayTemplateGenerator(('gwf6', 'disu', 'connectiondata', 
                                   'hwva'))
    angldegx = ArrayTemplateGenerator(('gwf6', 'disu', 'connectiondata', 
                                       'angldegx'))
    verticesrecarray = ListTemplateGenerator(('gwf6', 'disu', 'vertices', 
                                              'verticesrecarray'))
    cell2drecarray = ListTemplateGenerator(('gwf6', 'disu', 'cell2d', 
                                            'cell2drecarray'))
    package_abbr = "gwfdisu"
    package_type = "disu"
    dfn = [["block options", "name length_units", "type string", 
            "reader urword", "optional true"],
           ["block options", "name nogrb", "type keyword", "reader urword", 
            "optional true"],
           ["block options", "name xorigin", "type double precision", 
            "reader urword", "optional true"],
           ["block options", "name yorigin", "type double precision", 
            "reader urword", "optional true"],
           ["block options", "name angrot", "type double precision", 
            "reader urword", "optional true"],
           ["block dimensions", "name nodes", "type integer", 
            "reader urword", "optional false"],
           ["block dimensions", "name nja", "type integer", "reader urword", 
            "optional false"],
           ["block dimensions", "name nvert", "type integer", 
            "reader urword", "optional true"],
           ["block griddata", "name top", "type double precision", 
            "shape (nodes)", "reader readarray"],
           ["block griddata", "name bot", "type double precision", 
            "shape (nodes)", "reader readarray"],
           ["block griddata", "name area", "type double precision", 
            "shape (nodes)", "reader readarray"],
           ["block connectiondata", "name iac", "type integer", 
            "shape (nodes)", "reader readarray"],
           ["block connectiondata", "name ja", "type integer", 
            "shape (nja)", "reader readarray"],
           ["block connectiondata", "name ihc", "type integer", 
            "shape (nja)", "reader readarray"],
           ["block connectiondata", "name cl12", "type double precision", 
            "shape (nja)", "reader readarray"],
           ["block connectiondata", "name hwva", "type double precision", 
            "shape (nja)", "reader readarray"],
           ["block connectiondata", "name angldegx", 
            "type double precision", "optional true", "shape (nja)", 
            "reader readarray"],
           ["block vertices", "name verticesrecarray", 
            "type recarray iv xv yv", "reader urword", "optional false"],
           ["block vertices", "name iv", "type integer", "in_record true", 
            "tagged false", "reader urword", "optional false"],
           ["block vertices", "name xv", "type double precision", 
            "in_record true", "tagged false", "reader urword", 
            "optional false"],
           ["block vertices", "name yv", "type double precision", 
            "in_record true", "tagged false", "reader urword", 
            "optional false"],
           ["block cell2d", "name cell2drecarray", 
            "type recarray icell2d xc yc ncvert icvert", "reader urword", 
            "optional false"],
           ["block cell2d", "name icell2d", "type integer", 
            "in_record true", "tagged false", "reader urword", 
            "optional false"],
           ["block cell2d", "name xc", "type double precision", 
            "in_record true", "tagged false", "reader urword", 
            "optional false"],
           ["block cell2d", "name yc", "type double precision", 
            "in_record true", "tagged false", "reader urword", 
            "optional false"],
           ["block cell2d", "name ncvert", "type integer", "in_record true", 
            "tagged false", "reader urword", "optional false"],
           ["block cell2d", "name icvert", "type integer", "shape (ncvert)", 
            "in_record true", "tagged false", "reader urword", 
            "optional false"]]

    def __init__(self, model, add_to_package_list=True, length_units=None,
                 nogrb=None, xorigin=None, yorigin=None, angrot=None,
                 nodes=None, nja=None, nvert=None, top=None, bot=None,
                 area=None, iac=None, ja=None, ihc=None, cl12=None, hwva=None,
                 angldegx=None, verticesrecarray=None, cell2drecarray=None,
                 fname=None, pname=None, parent_file=None):
        super(ModflowGwfdisu, self).__init__(model, "disu", fname, pname,
                                             add_to_package_list, parent_file)        

        # set up variables
        self.length_units = self.build_mfdata("length_units",  length_units)
        self.nogrb = self.build_mfdata("nogrb",  nogrb)
        self.xorigin = self.build_mfdata("xorigin",  xorigin)
        self.yorigin = self.build_mfdata("yorigin",  yorigin)
        self.angrot = self.build_mfdata("angrot",  angrot)
        self.nodes = self.build_mfdata("nodes",  nodes)
        self.nja = self.build_mfdata("nja",  nja)
        self.nvert = self.build_mfdata("nvert",  nvert)
        self.top = self.build_mfdata("top",  top)
        self.bot = self.build_mfdata("bot",  bot)
        self.area = self.build_mfdata("area",  area)
        self.iac = self.build_mfdata("iac",  iac)
        self.ja = self.build_mfdata("ja",  ja)
        self.ihc = self.build_mfdata("ihc",  ihc)
        self.cl12 = self.build_mfdata("cl12",  cl12)
        self.hwva = self.build_mfdata("hwva",  hwva)
        self.angldegx = self.build_mfdata("angldegx",  angldegx)
        self.verticesrecarray = self.build_mfdata("verticesrecarray", 
                                                  verticesrecarray)
        self.cell2drecarray = self.build_mfdata("cell2drecarray", 
                                                cell2drecarray)
