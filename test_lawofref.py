import numpy as np
import matplotlib.pyplot as plt
import sympy

class ReflectionPlot:
    def __init__(self):
        # Generate random points for function
        self.xy_values = np.random.rand(5, 2)

        def f(x_val, y_val):
            return x_val ** 2 + y_val ** 2 + 5

        self.f = f
        result = np.apply_along_axis(lambda x_val: self.f(x_val[0], x_val[1]),
                                     1, self.xy_values)
        print(result)
    def calculate_derivatives(self):
        # Derivative for calculating x_val,y_val
        x_val = sympy.Symbol('x_val')
        y_val = sympy.Symbol('y_val')
        dfdx = sympy.diff(self.f(x_val, y_val), x_val)
        dfdy = sympy.diff(self.f(x_val, y_val), y_val)

        p = np.apply_along_axis(lambda xy: dfdx.subs([(x_val, xy[0]), (y_val, xy[1])]),
                            1, self.xy_values)
        q = np.apply_along_axis(lambda xy: dfdy.subs([(x_val, xy[0]), (y_val, xy[1])]),
                            1, self.xy_values)
        n_const = -1
        self.normal = np.concatenate(
            (p[np.newaxis, :], q[np.newaxis, :], n_const * np.ones((1, np.size(p)))),
            axis=0)

    def calculate_reflection(self):
        # Passes xy values to given function



        x_val = np.linspace(-1, 1, 10)
        y_val = np.linspace(-1, 1, 10)
        X, Y = np.meshgrid(x_val, y_val)

        Z = self.f(X, Y)
        s_incident = np.array([0, 0, 1])
        P = self.xy_values + s_incident[np.newaxis, :2] * self.f(self.xy_values[:, 0],
                                                       self.xy_values[:, 1])[:, np.newaxis]
        P_3D = np.hstack((P, self.f(self.xy_values[:, 0],self.xy_values[:, 1])[:,np.newaxis]))


        # Calculate magnitude of Normal
        normal = self.normal.astype(float)
        magnitude_of_normal = np.sqrt(
            normal[0, :] ** 2 + normal[1, :] ** 2 + normal[2, :] ** 2)
        mag = np.tile(magnitude_of_normal, (3, 1))
        norm_hat = normal / mag

        # Calculate reflection
        s_incident = np.transpose(np.resize(s_incident, (5, 3)))
        ref = np.tile(2 * (np.sum(s_incident * norm_hat, axis=0)), (3, 1))
        reflection = s_incident - ref * norm_hat

        # Plot
        fig = plt.figure()
        ax = plt.axes(projection='3d')
        ax.plot_surface(X, Y, Z, cmap='rainbow')
        ax.scatter(P_3D[:, 0], P_3D[:, 1], P_3D[:, 2], s=50, color='black')
        for i in range(5):
            plt.plot([self.xy_values[i, 0], P_3D[i, 0]], [self.xy_values[i, 1], P_3D[i, 1]],
                     [0, P_3D[i, 2]])
        ax.set_title("3D Surface Plot")
        plt.scatter(self.xy_values[:, 0], self.xy_values[:, 1], s=50)
        plt.xlabel('x_val values')
        plt.ylabel('y_val values')
        plt.title('Rays from random point sources hits surface with n normal')
        plt.axis("equal")
        for i in range(5):
            ax.quiver(P_3D[i, 0], P_3D[i, 1], P_3D[i, 2], norm_hat[0, i], norm_hat[
                1, i], norm_hat[2, i], color='r')
            ax.quiver(P_3D[i, 0], P_3D[i, 1], P_3D[i, 2], reflection[0, i],
                      reflection[1, i], reflection[2, i], color='y')
        plt.show()
