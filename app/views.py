"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from django.core.paginator import Paginator
import pandas as pd
from . import data

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    
    df = data.getData();
    table_class = 'table table-striped table-hover table-responsive'
    
    # Set up pagination
    paginator = Paginator(df.values, 10)  # Show 10 rows per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    table = pd.DataFrame(page_obj.object_list, columns=df.columns).to_html(render_links=True,classes=table_class, index=False, escape=False)
    return render(
        request,
        'app/index.html',
        {
            'title':'Title Aggregator',
            'year':datetime.now().year,
            'table': table,
            'page_obj': page_obj
        }
    )