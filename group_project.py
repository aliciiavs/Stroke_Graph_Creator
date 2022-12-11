import pandas as pd
import matplotlib.pyplot as plt
from graphics import *

win = GraphWin('Programming Project', 900, 750)


def clear(window):
    for element in window.items[:]:
        element.undraw()
    window.update()


def button_creator(text, a1=350, a2=400, b1=550, b2=450):
    not_clicked = True

    button = Rectangle(Point(a1, a2), Point(b1, b2))
    click = Text(Point(((a1 + b1) / 2), ((a2 + b2) / 2)), text)
    button.draw(win)
    click.draw(win)

    while not_clicked:
        pt = win.getMouse()
        if a1 < pt.getX() < b1:
            if a2 < pt.getY() < b2:
                clear(win)
                not_clicked = False


def fake_button(button_text, a1=350, a2=400, b1=550, b2=450):
    button = Rectangle(Point(a1, a2), Point(b1, b2))
    click = Text(Point(((a1 + b1) / 2), ((a2 + b2) / 2)), button_text)
    button.setOutline('gray25')
    click.setTextColor('gray25')
    button.draw(win)
    click.draw(win)


def reader(window, display=True):  # it rewrites bc it already exists
    with open("C:/Users/usuario/Desktop/bdba/python_programming/project/"
              "healthcare-dataset-stroke-data.csv") as data_frame:
        df = pd.read_csv(data_frame)
        if display:
            n = 0
            for line in df:
                time.sleep(0.05)
                n += 20
                point = Point(450, 200 + n)
                x = Text(point, line)
                x.draw(window)
                if point.getY() > 600:
                    clear(window)
                    break
        else:
            return df


csv_read = reader(win, display=False)
data = pd.DataFrame(csv_read, columns=['id', 'hypertension', 'heart_disease', 'ever_married', 'work_type',
                                       'Residence_type', 'avg_glucose_level', 'gender', 'age', 'bmi',
                                       'smoking_status', 'stroke'])

# altering hypertension values to yes and no
data['hypertension'].replace(to_replace=1, value="Yes", inplace=True)
data['hypertension'].replace(to_replace=0, value="No", inplace=True)

# altering heart_disease values to yes and no
data['heart_disease'].replace(to_replace=1, value="Yes", inplace=True)
data['heart_disease'].replace(to_replace=0, value="No", inplace=True)

# altering heart_disease values to yes and no
data['stroke'].replace(to_replace=1, value="Yes", inplace=True)
data['stroke'].replace(to_replace=0, value="No", inplace=True)

data = data.dropna()


def initial():
    win.setBackground('indianred1')

    title = Text(Point(win.getWidth() / 2, 250), 'WELCOME')
    title.setFace('helvetica')
    title.setStyle('bold')
    title.setSize(25)

    message = Text(Point(win.getWidth() / 2, 350), 'This program allows for the creation of'
                                                   ' charts for healthcare stroke data.')
    message.setFace('helvetica')
    message.setSize(11)

    title.draw(win)
    message.draw(win)

    button_creator('Click to upload CSV', a2=450, b2=500)
    reader(win)
    clear(win)


def plot_displayer(page_title, clicker_1, clicker_2, clicker_3):
    win.setBackground('indianred2')

    title = Text(Point(win.getWidth() / 2, 200), page_title)
    title.setFace('helvetica')
    title.setSize(15)
    title.draw(win)

    x_circle = 350
    y_circle = 300
    rad = 45

    plot1 = Circle(Point(x_circle, y_circle), rad)  # scatter plot
    plot1.setFill('skyblue')
    tex1 = Text(Point(x_circle, y_circle), clicker_1)
    plot1.draw(win)
    tex1.draw(win)

    plot2 = plot1.clone()  # pie chart
    plot2.move(100, 0)
    tex2 = Text(Point(x_circle + 100, y_circle), clicker_2)
    plot2.draw(win)
    tex2.draw(win)

    plot3 = plot1.clone()  # bar plot
    plot3.move(200, 0)
    tex3 = Text(Point(x_circle + 200, y_circle), clicker_3)
    plot3.draw(win)
    tex3.draw(win)

    fake_button('Click to proceed')

    scatter = False
    pie = False
    bar = False

    selected = False

    while not selected:
        picked = False
        pt = win.getMouse()
        if y_circle - rad < pt.getY() < y_circle + rad:
            if x_circle - rad < pt.getX() < x_circle + rad:
                plot1.setFill('skyblue3')
                picked = True
                scatter = True
                pie = False
                bar = False
                pt = win.getMouse()
            elif x_circle - rad + 100 < pt.getX() < x_circle + rad + 100:
                plot2.setFill('skyblue3')
                picked = True
                scatter = False
                pie = True
                bar = False
                pt = win.getMouse()
            elif x_circle - rad + 200 < pt.getX() < x_circle + rad + 200:
                plot3.setFill('skyblue3')
                picked = True
                scatter = False
                pie = False
                bar = True
                pt = win.getMouse()

        if picked and 350 < pt.getX() < 550:
            if 400 < pt.getY() < 450:
                break

        if picked and y_circle - rad < pt.getY() < y_circle + rad:
            if x_circle - rad < pt.getX() < x_circle + rad:
                plot1.setFill('skyblue')
                scatter = False
                pie = False
                bar = False
            elif x_circle - rad + 100 < pt.getX() < x_circle + rad + 100:
                plot2.setFill('skyblue')
                scatter = False
                pie = False
                bar = False
            elif x_circle - rad + 200 < pt.getX() < x_circle + rad + 200:
                plot3.setFill('skyblue')
                scatter = False
                pie = False
                bar = False

    button_creator('Click to proceed')
    plot_code = 0
    if scatter:
        plot_code = 1
    elif pie:
        plot_code = 2
    elif bar:
        plot_code = 3
    return 'plot' + str(plot_code)


def insert_button(default_text, first_box_text=None, second_box_text=None, a1=350, a2=400):
    input_text_x = None

    if first_box_text is not None:
        Text(Point(a1 + 50, a2 + 50), first_box_text).draw(win)
        input_text_x = Entry(Point(a1 + 200, a2 + 50), 10)
        input_text_x.setText(default_text)
        input_text_x.draw(win)

    input_text_y = None

    if second_box_text is not None:
        Text(Point(a1 + 50, a2 + 100), second_box_text).draw(win)
        input_text_y = Entry(Point(a1 + 200, a2 + 100), 10)
        input_text_y.setText(default_text)
        input_text_y.draw(win)

    output_text = Text(Point(a1 + 200, a2 + 200), '')
    output_text.draw(win)

    selected = Text(Point(a1 + 50, a2 + 200), 'Variable(s) chosen: ')
    selected.draw(win)

    button = Rectangle(Point((win.getWidth() / 2) - 50, a2 + 140), Point((win.getWidth() / 2) + 50, a2 + 160))
    click = Text(Point(win.getWidth() / 2, a2 + 150), 'Select')

    button.setFill('indianred3')
    button.setOutline('indianred3')
    button.draw(win)
    click.draw(win)

    win.getMouse()

    value_list_x = []

    if value_list_x is not None:
        if input_text_x is not None:
            values_x = input_text_x.getText()
            value_list_x = values_x.split(',')
            value_list_x = [str(x) for x in value_list_x]

    value_list_y = []

    if second_box_text is not None:
        if input_text_y is not None:
            values_y = input_text_y.getText()
            value_list_y = values_y.split(',')
            value_list_y = [str(x) for x in value_list_y]

    value_list = value_list_x + value_list_y

    output_text.setText(value_list)

    return value_list


def variable_picking_for_plot(page_title, variable_name_cond1, default_text_in_insert_box,
                              box_1_title, box_2_title, variable_name_cond2=None,
                              page_text='Choose two variables you wish to plot', second_condition=False):

    title = Text(Point(win.getWidth() / 2, 50), page_title)
    text = Text(Point(win.getWidth() / 2, 150), page_text)

    title.setFace('helvetica')
    title.setSize(25)
    text.setFace('helvetica')
    text.setSize(15)
    title.draw(win)
    text.draw(win)

    # display correct variables
    possible_variables = data.dtypes[data.dtypes == variable_name_cond1].index.values.tolist()

    possible_variables_cond2 = []
    if second_condition:
        possible_variables_cond2 = data.dtypes[data.dtypes == variable_name_cond2].index.values.tolist()

    n = 0
    m = 0
    if second_condition:
        m = -75

    for i in possible_variables:
        n += 30
        column = Text(Point(450 + m, 175 + n), i)
        column.setSize(9)
        column.draw(win)

    if second_condition:
        m = 0
        for j in possible_variables_cond2:
            m += 30
            column_2 = Text(Point(525, 175 + m), j)
            column_2.setSize(9)
            column_2.draw(win)

    x = insert_button(default_text_in_insert_box, box_1_title, box_2_title)

    button_creator('Continue', a2=650, b2=700)

    return x


def pie_chart():
    title = Text(Point(win.getWidth() / 2, 50), 'PIE CHART')
    text = Text(Point(win.getWidth() / 2, 100), 'Choose ONE categorical variable:   ')
    title.setFace('helvetica')
    title.setSize(25)
    text.setFace('helvetica')
    text.setSize(15)
    title.draw(win)
    text.draw(win)


def bar_plot():
    title = Text(Point(win.getWidth() / 2, 50), 'BAR PLOT')
    text = Text(Point(win.getWidth() / 2, 100), 'Choose the variables you wish to plot')
    title.setFace('helvetica')
    title.setSize(25)
    text.setFace('helvetica')
    text.setSize(15)
    title.draw(win)
    text.draw(win)


def plot_titles_editor(default_plot, default_title, chosen_x, chosen_y, title=True, edit_1_name='Edit x label: ',
                       edit_2_name='Edit y label: ', a1=450, a2=350):
    default_plot = Image(Point(330, 350), default_plot)
    default_plot.draw(win)

    # edit title
    edit_title = Text(Point(a1 + 250, a2 - 200), 'Edit title: ')
    input_title = Entry(Point(a1 + 360, a2 - 200), 11)
    input_title.setText(default_title)
    if title:
        edit_title.draw(win)
        input_title.draw(win)

    # edit x label
    edit_x_label = Text(Point(a1 + 260, a2 - 100), edit_1_name)
    edit_x_label.draw(win)
    input_x_label = Entry(Point(a1 + 360, a2 - 100), 11)
    input_x_label.setText(chosen_x)
    input_x_label.draw(win)

    # edit y label
    edit_y_label = Text(Point(a1 + 260, a2), edit_2_name)
    edit_y_label.draw(win)
    input_y_label = Entry(Point(a1 + 360, a2), 11)
    input_y_label.setText(chosen_y)
    input_y_label.draw(win)

    fake_button('Edit', a1=680, b1=850)
    win.getMouse()

    inputted_title = ''

    if title:
        inputted_title = input_title.getText()
    inputted_x_label = input_x_label.getText()
    inputted_y_label = input_y_label.getText()

    changes = [inputted_title, inputted_x_label, inputted_y_label]

    button_creator('Edit', a1=680, b1=850)

    return changes


def plot_point_editor(a1=450, a2=350):

    # choose your color
    edit_title = Text(Point(a1 + 250, a2 - 200), '   EDIT YOUR MARKER')
    edit_title.draw(win)

    # colors display
    marker_options = Image(Point(330, 350), 'math_plot_markers.png')
    marker_options.draw(win)

    choose_marker = Text(Point(a1 + 200, a2 - 100), ' Choose marker: ')
    choose_marker.draw(win)
    input_choose_marker = Entry(Point(a1 + 350, a2 - 100), 10)
    input_choose_marker.setText('default')
    input_choose_marker.draw(win)

    choose_color = Text(Point(a1 + 190, a2 - 50), 'Choose color: ')
    colors_to_be_chosen = Text(Point(a1 + 275, a2), 'Options are blue, green, red, cyan,\n magenta, yellow,'
                                                    ' black or white')
    choose_color.draw(win)
    colors_to_be_chosen.draw(win)
    input_choose_color = Entry(Point(a1 + 350, a2 - 50), 10)
    input_choose_color.setText('default')
    input_choose_color.draw(win)

    fake_button('Next', a1=700, b1=800)
    win.getMouse()

    marker = input_choose_marker.getText()
    color = input_choose_color.getText()

    marker_for_python = "^"
    color_for_python = "g"

    if marker != "default":
        marker_for_python = shapes.get(marker)
    if color != "default":
        color_for_python = colors.get(color)

    button_creator('Next', a1=700, b1=800)

    edits = [color_for_python, marker_for_python]

    return edits


colors = {"blue": "b", "green": "g", "red": "r", "cyan": "c", "magenta": "m", "yellow": "y", "black": "k",
          "white": "w"}

shapes = {"point": ".", "pixel": ",", "circle": "o", "triangle_down": "v", "triangle_up": "^", "triangle_left": "<",
          "triangle_right": ">", "tri_down": "1", "tri_up": "2", "tri_left": "3", "tri_right": "4", "octagon": "8",
          "square": "s", "pentagon": "p", "filled plus": "P", "star": "*", "hexagon1": "h", "hexagon2": "H",
          "plus": "+", "x": "x", "filled x": "X", "thin diamond": "d", "diamond": "D", "vline": "|", "hline": "_"}


def add_legend():

    answer = plot_displayer('Do you wish to add a legend?', 'Of course', 'I guess...', 'No')

    if answer == 'plot1' or answer == 'plot2':
        return True


def scatter_plot_creator(x, y, title='Default', x_label="default x-label", y_label="default y-label", color="g",
                         marker="^", button_box='Next'):

    data.plot.scatter(x=str(x), y=str(y), c=color, marker=marker)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.ioff()
    plt.savefig('scatter_plot.png', format='png')
    scatter_plot = Image(Point(450, 350), 'scatter_plot.png')
    scatter_plot.draw(win)

    button_creator(button_box, a2=650, b2=700)


def pie_chart_creator(x, title='Default', title_color='black', title_size=30, button_box='Next'):
    data[x].value_counts([x]).plot(kind='pie', autopct='%1.1f%%', shadow=True)
    centre_circle = plt.Circle((0, 0), 0.30, fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)
    plt.title(title, color=title_color, family='serif', fontsize=title_size)

    plt.ioff()
    plt.savefig('pie_chart.png', format='png')
    pie_chart_ = Image(Point(450, 350), 'pie_chart.png')
    pie_chart_.draw(win)

    button_creator(button_box, a2=650, b2=700)


def bar_plot_creator(scalar_variable, categorical_variable, title="Average {scalar_variable} by {categorical_variable}",
                     x_label="{categorical_variable}", y_label="Average of {scalar_variable}", col=None,
                     button_box='Next'):
    if col is None:
        col = ['green']
    grouped = data.groupby(categorical_variable)[scalar_variable]

    averaged_groups = {i[0]: sum(i[1])/len(i[1]) for i in grouped}

    names = list(averaged_groups.keys())
    values = list(averaged_groups.values())
    plt.bar(range(len(averaged_groups)), values, tick_label=names, color=col)
    plt.ylabel(y_label)
    plt.xlabel(x_label)
    plt.title(title)
    plt.ioff()
    plt.savefig('bar_plot.png', format='png')
    bar_plot_ = Image(Point(450, 350), 'bar_plot.png')
    bar_plot_.draw(win)

    button_creator(button_box, a2=650, b2=700)


def main():
    logo = Image(Point(win.getWidth() / 2, 100), "no_back_logo_resized.png")
    logo.draw(win)
    initial()

    output = plot_displayer('Which plot do you wish to create?', 'Scatter plot', 'Pie chart', 'Bar plot')
    # Python dtype arguments: object (for strings), int64 (for integers), float64(for floats), bool (for booleans)
    if output == 'plot1':
        selected_variables = variable_picking_for_plot('SCATTER PLOT', 'float64', 'age',
                                                       box_1_title='Variable for x axis: ',
                                                       box_2_title='Variable for y axis: ')
        x = selected_variables[0]
        y = selected_variables[1]
        scatter_plot_creator(x, y)
        titles_changes = plot_titles_editor(default_plot='scatter_plot.png', default_title=x + ' vs. ' + y,
                                            chosen_x=x, chosen_y=y)
        scatter_plot_creator(x, y, title=titles_changes[0], x_label=titles_changes[1], y_label=titles_changes[2])
        point_changes = plot_point_editor()
        scatter_plot_creator(x, y, title=titles_changes[0], x_label=titles_changes[1], y_label=titles_changes[2],
                             color=point_changes[0], marker=point_changes[1], button_box='Finalize')

    elif output == 'plot2':
        selected_variable = variable_picking_for_plot('PIE CHART', 'object', 'stroke',
                                                      box_1_title=None,
                                                      box_2_title='Pick ONE categorical variable:   ',
                                                      page_text='Choose the variable you wish to plot')
        x = selected_variable[0]
        pie_chart_creator(x)
        titles_changes = plot_titles_editor(default_plot='pie_chart.png', default_title=x, chosen_x='black',
                                            chosen_y=20,
                                            edit_1_name='Edit title color: ', edit_2_name='Edit title size: ')
        pie_chart_creator(x, title=titles_changes[0], title_color=titles_changes[1], title_size=titles_changes[2],
                          button_box='Finalize')

    elif output == 'plot3':
        selected_variables = variable_picking_for_plot('BAR PLOT', 'object', 'stroke',
                                                       box_1_title='Pick variable from column 1:   ',
                                                       box_2_title='Pick variable from column 2:   ',
                                                       variable_name_cond2='float64',
                                                       page_text='Choose two variables you wish to plot',
                                                       second_condition=True)
        scalar_variable = selected_variables[1]
        categorical_variable = selected_variables[0]
        bar_plot_creator(scalar_variable, categorical_variable)
        titles_changes = plot_titles_editor(default_plot='bar_plot.png',
                                            default_title=f"Average {scalar_variable} by {categorical_variable}",
                                            chosen_x=f"{categorical_variable}",
                                            chosen_y=f"Average {scalar_variable}",
                                            edit_1_name='Edit x-label: ', edit_2_name='Edit y-label: ')
        bar_plot_creator(scalar_variable, categorical_variable, titles_changes[0], titles_changes[1], titles_changes[2],
                         button_box='Next')
        bar_colors = plot_titles_editor(default_plot='bar_plot.png',
                                        default_title='Pick the color for each bar: ',
                                        chosen_x='magenta',
                                        chosen_y='green', title=False,
                                        edit_1_name='Pick color 1: ',
                                        edit_2_name='Pick color 2: ')
        bar_plot_creator(scalar_variable, categorical_variable, titles_changes[0], titles_changes[1], titles_changes[2],
                         col=[bar_colors[1], bar_colors[2]], button_box='Finalize')


main()
