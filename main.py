import plotly.graph_objects as go
from s_orbital import generate_s_orbital
from p_orbital import generate_p_orbital
from d_orbital import generate_d_orbital


def plot_orbital(x, y, z, title):
    fig = go.Figure(data=[go.Surface(x=x, y=y, z=z)])

    fig.update_layout(
        title=title,
        scene=dict(
            xaxis_title='X',
            yaxis_title='Y',
            zaxis_title='Z'
        )
    )

    fig.show()


def main():
    print("Orbital Shape Visualizer")
    print("1. s-orbital")
    print("2. p-orbital")
    print("3. d-orbital")

    choice = input("Enter your choice: ")

    if choice == '1':
        x, y, z = generate_s_orbital()
        plot_orbital(x, y, z, "s-Orbital")

    elif choice == '2':
        x, y, z = generate_p_orbital()
        plot_orbital(x, y, z, "p-Orbital")

    elif choice == '3':
        x, y, z = generate_d_orbital()
        plot_orbital(x, y, z, "d-Orbital")

    else:
        print("Invalid choice!")


if __name__ == "__main__":
    main()
    
