using LinearAlgebra
include("qr_factorisation.jl")


function find_eigenvalues(A::Matrix, repeats::Int)::Tuple{Matrix, Matrix}
    A_k = copy(A)
    n = size(A)[1]
    QQ = Diagonal(ones(n))
    for k in repeats
        s = A_k[n-1, n-1]
        smult = s * Diagonal(ones(n))
        Q, R = gram_schmidt(A_k - smult)

        A_k = R * Q + smult

        QQ = QQ * Q

        if k % 10000 == 0
            print("A, k = " * string(k))
            display("text/plain", A_k)
        end
    end
    return A_k, QQ
end


if Main == @__MODULE__
    A = [1.0 2.0 3.0; 4.0 5.0 6.0; 7.0 8.0 9.0]
    find_eigenvalues(A, 500000)
end