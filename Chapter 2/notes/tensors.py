from fpdf import FPDF

# Create instance of FPDF class
pdf = FPDF()

# Add a page
pdf.add_page()

# Set title
pdf.set_font("Arial", 'B', 16)
pdf.cell(200, 10, txt="Tensors in Deep Learning and PyTorch", ln=True, align='C')

# Add a line break
pdf.ln(10)

# Set content font
pdf.set_font("Arial", size=12)

# Add content
content = """
A tensor is a multi-dimensional generalization of scalars, vectors, and matrices.
It is the core data structure used in deep learning frameworks like PyTorch and TensorFlow.

Types of Tensors:

1. Scalar (0D Tensor)
   - A scalar is a single value or number.
   - Example: 5, -3.14
   - PyTorch Example:
   tensor = torch.tensor(5)  # 0D tensor

2. Vector (1D Tensor)
   - A vector is a 1-dimensional array of numbers.
   - Example: [1, 2, 3, 4]
   - PyTorch Example:
   vector = torch.tensor([1, 2, 3, 4])  # 1D tensor

3. Matrix (2D Tensor)
   - A matrix is a 2-dimensional array of numbers (rows and columns).
   - Example: [[1, 2], [3, 4], [5, 6]]
   - PyTorch Example:
   matrix = torch.tensor([[1, 2], [3, 4], [5, 6]])  # 2D tensor

4. Higher-dimensional Tensor
   - A tensor can have more than two dimensions. For example, a 3D tensor could represent a stack of matrices.
   - Example (3D Tensor): [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
   - PyTorch Example:
   tensor_3d = torch.tensor([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])  # 3D tensor

Why Are Tensors Important?

1. Flexibility:
   - Tensors allow for representation of different data types (like images, videos, or text) in deep learning.

2. Efficient Computation:
   - Tensors enable highly optimized computations, especially when used with hardware accelerators like GPUs.

3. Mathematical Operations:
   - Tensors support a wide range of mathematical operations (like addition, multiplication, etc.) that are essential in machine learning and deep learning.

Tensor Operations in PyTorch:

1. Creating Tensors:
   - You can create tensors from Python lists, NumPy arrays, or other tensors.
   - PyTorch Example:
   tensor = torch.tensor([1, 2, 3])  # Creating a tensor from a list

2. Basic Operations:
   - PyTorch allows for element-wise operations like addition, multiplication, etc.
   - Example:
   tensor1 = torch.tensor([1, 2, 3])
   tensor2 = torch.tensor([4, 5, 6])
   result = tensor1 + tensor2  # Element-wise addition

3. Reshaping Tensors:
   - You can change the shape of a tensor using .reshape() or .view().
   - Example:
   tensor = torch.tensor([1, 2, 3, 4, 5, 6])
   reshaped_tensor = tensor.reshape(2, 3)  # Reshaping to a 2x3 matrix
"""

# Add content to PDF
pdf.multi_cell(0, 10, content)

# Save PDF to file
pdf_output_path = "/mnt/data/tensors_in_deep_learning.pdf"
pdf.output(pdf_output_path)

pdf_output_path