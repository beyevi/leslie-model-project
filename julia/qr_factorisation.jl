using LinearAlgebra


"""
Perform Gram-Schmidt algorithm to find a QR-factorisation
for some matrix A of size ``m × n``.

# Arguments
- `A::Matrix`: The input matrix for which QR-factorization is computed.

# Returns
- `Q::Matrix`:  an ``m × n`` matrix with orthonormal columns
- `R::Matrix`:  an upper-triangular ``n × n`` matrix
"""
function gram_schmidt(A::Matrix)::Tuple{Matrix, Matrix}
    m, n = size(A)
    Q = similar(A, m, n)
    R = zeros(Float64, n, n)

    for i in 1:n
        v = copy(A[:, i])
        for j in 1:(i-1)
            R[j, i] = dot(Q[:, j], A[:, i])
            v -= R[j, i] * Q[:, j]
        end
        R[i, i] = Float64(norm(v))
        Q[:, i] = v / R[i, i]
    end

    return Q, R
end


if Main == @__MODULE__
    A = [1.0 2.0 3.0; 4.0 5.0 6.0; 7.0 8.0 9.0]
    Q, R = gram_schmidt(A)

    println("Q is:")
    display("text/plain", Q)
    println()
    println("R is:")
    display("text/plain", R)
end