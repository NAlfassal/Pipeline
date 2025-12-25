import plotly.express as px
from pathlib import Path

def bar_sorted(df, x, y, title):
    df_plot = df.sort_values(by=y, ascending=False)
    fig = px.bar(df_plot, x=x, y=y, title=title, template="plotly_white")
    fig.update_layout(title_x=0.05) # تحريك العنوان قليلاً لليسار
    return fig

def time_line(df, x, y, title):
    fig = px.line(df, x=x, y=y, title=title, markers=True)
    return fig

def histogram_chart(df, x, nbins, title):
    fig = px.histogram(df, x=x, nbins=nbins, title=title, opacity=0.85)
    fig.update_layout(bargap=0.05)
    return fig

def save_fig(fig, path: Path, scale=2):
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.write_image(str(path), scale=scale)