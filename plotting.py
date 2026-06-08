import matplotlib.pyplot as plt

def render_plot(finalValues):

    print("Rendering Plot")
    fig, ax = plt.subplots(figsize=(8, 6))

    split_index = len(finalValues) // 2


    for i, rAndMValues in enumerate(finalValues):
        if i < split_index:
            linestyle = '-'
        else:
            linestyle = '--'
        ax.plot(rAndMValues[0], rAndMValues[1], linestyle=linestyle, lw=2)

    plt.legend(['MDI-2', 'SkΙ4', 'SCVBB', 'W', 'DH', 'APR-1'], fontsize=10, ncol=1) # Please change it depending on the EOS you use.

    plt.xlabel(r'Radius $\rm{(km)}$',fontsize=22)
    plt.ylabel(r'Mass $\rm (M_{\odot})$', fontsize=22)
    plt.xlim(7,20)
    plt.ylim(-0.1,2.7)
    plt.grid(False)
    plt.tight_layout()
    plt.show()


