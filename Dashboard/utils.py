# Esta función añade características a los layouts para que tengan todos algunas características comunes y fáciles de cambiar
from variables import *


def layout_additions(fig):

    fig.update_layout(paper_bgcolor="#FAF9F9")
    fig.update_layout(legend=dict(font=dict(size=legend_size)))

    return fig
