# Copyright (c) 2025, NVIDIA CORPORATION & AFFILIATES. ALL RIGHTS RESERVED.
#
# SPDX-License-Identifier: LicenseRef-NVIDIA-SOFTWARE-LICENSE

from cuda.core.experimental import Device, system


def _bool_str(value: bool) -> str:
    return "YES" if value else "NO"


def _bytes_to_mbytes(value):
    return f"{value * 9.5367431640625e-7:.2f}MB"


def _bytes_to_gbytes(value):
    return f"{value * 9.313225746154785e-10:.2f}GB"


def print_device_properties(properties):
    print("Properties:\n------------")
    print(f"- Can map host memory into the CUDA address space: {_bool_str(properties.can_map_host_memory)}")
    print(f"- Can access host registered memory at the same virtual address as the CPU: \
          {_bool_str(properties.can_use_host_pointer_for_registered_mem)}")
    print(f"- Clock rate: {properties.clock_rate * 1e-6:.2f}GHz")
    print(f"- Peak memory clock frequency: {properties.memory_clock_rate * 1e-6:.2f}GHz")
    print(f"- Performance ratio (single precision)/(double precision): \
          {properties.single_to_double_precision_perf_ratio}")
    print(f"- Compute capability: major={properties.compute_capability_major}, \
          minor={properties.compute_capability_minor}")
    print(f"- Compute mode: {properties.compute_mode} (0 - default, 2 - prohibited, 3 - exclusive process)")
    print(f"- Support for Compute Preemption: {_bool_str(properties.compute_preemption_supported)}")
    print(f"- Support for concurrent kernels execution within the same context: \
          {_bool_str(properties.concurrent_kernels)}")
    print(f"- Support for coherent access to managed memory concurrently with CPU: \
          {_bool_str(properties.concurrent_managed_access)}")
    print(f"- Support for deferred mapping in CUDA arrays and CUDA mipmapped arrays: \
          {_bool_str(properties.deferred_mapping_cuda_array_supported)}")
    print(f"- Support for direct access of managed memory on device without migration: \
            {_bool_str(properties.direct_managed_mem_access_from_host)}")
    print(f"- ECC enabled: {_bool_str(properties.ecc_enabled)}")
    print(f"- Support for generic compression: {_bool_str(properties.generic_compression_supported)}")
    print(f"- Support for caching globals in L1 cache: {_bool_str(properties.global_l1_cache_supported)}")
    print(f"- Support for caching locals in L1 cache: {_bool_str(properties.local_l1_cache_supported)}")
    print(f"- Global memory bus widths: {properties.global_memory_bus_width} bits")
    print(f"- Support for GPUDirect RDMA: {_bool_str(properties.gpu_direct_rdma_supported)}")
    print(f"- GPUDirect RDMA flush-writes options bitmask: 0b{properties.gpu_direct_rdma_flush_writes_options:032b}")
    print(f"- GPUDirect RDMA writes ordering: {properties.gpu_direct_rdma_writes_ordering} \
          (0 - none, 100 - this device can consume remote writes, \
          200 - any CUDA device can consume remote writes to this device)")
    print(f"- Can concurrently copy memory between host and device while executing kernel: \
          {_bool_str(properties.gpu_overlap)}")
    print(f"- Support for exporting memory to a posix file descriptor: \
          {_bool_str(properties.handle_type_posix_file_descriptor_supported)}")
    print(f"- Support for exporting memory to a Win32 NT handle: \
          {_bool_str(properties.handle_type_win32_handle_supported)}")
    print(f"- Support for exporting memory to a Win32 KMT handle: \
          {_bool_str(properties.handle_type_win32_kmt_handle_supported)}")
    print(f"- Link between device and host supports native atomic operations: \
          {_bool_str(properties.host_native_atomic_supported)}")
    print(f"- Device is integrated with memory subsystem: {_bool_str(properties.integrated)}")
    print(f"- Kernel execution timeout: {_bool_str(properties.kernel_exec_timeout)}")
    print(f"- L2 cache size: {_bytes_to_mbytes(properties.l2_cache_size)}")
    print(f"- Max L2 persisting lines capacity: {_bytes_to_mbytes(properties.max_persisting_l2_cache_size)}")
    print(f"- Support for managed memory allocation: {_bool_str(properties.managed_memory)}")
    print(f"- Max access policy window size: {_bytes_to_mbytes(properties.max_access_policy_window_size)}")
    print(f"- Max x-dimension of a block: {properties.max_block_dim_x}")
    print(f"- Max y-dimension of a block: {properties.max_block_dim_y}")
    print(f"- Max z-dimension of a block: {properties.max_block_dim_z}")
    print(f"- Max blocks in a multiprocessor: {properties.max_blocks_per_multiprocessor}")
    print(f"- Max x-dimension of a grid: {properties.max_grid_dim_x}")
    print(f"- Max y-dimension of a grid: {properties.max_grid_dim_y}")
    print(f"- Max z-dimension of a grid: {properties.max_grid_dim_z}")
    print(f"- Max pitch allowed by the memory copy functions: {_bytes_to_gbytes(properties.max_pitch)}")
    print(f"- Max number of 32-bit registers per block: {properties.max_registers_per_block}")
    print(f"- Max number of 32-bit registers in a multiprocessor: {properties.max_registers_per_multiprocessor}")
    print(f"- Max shared memory per block: {properties.max_shared_memory_per_block}B")
    print(f"- Max optin shared memory per block: {properties.max_shared_memory_per_block_optin}B")
    print(f"- Max shared memory available to a multiprocessor: {properties.max_shared_memory_per_multiprocessor}B")
    print(f"- Max threads per block: {properties.max_threads_per_block}")
    print(f"- Max threads per multiprocessor: {properties.max_threads_per_multiprocessor}")
    print(f"- Warp size: {properties.warp_size}")
    print(f"- Max 1D surface width: {properties.maximum_surface1d_width}")
    print(f"- Max layers in 1D layered surface: {properties.maximum_surface1d_layered_layers}")
    print(f"- Max 1D layered surface width: {properties.maximum_surface1d_layered_width}")
    print(f"- Max 2D surface width: {properties.maximum_surface2d_width}")
    print(f"- Max 2D surface height: {properties.maximum_surface2d_height}")
    print(f"- Max layers in 2D layered surface: {properties.maximum_surface2d_layered_layers}")
    print(f"- Max 2D layered surface width: {properties.maximum_surface2d_layered_width}")
    print(f"- Max 2D layered surface height: {properties.maximum_surface2d_layered_height}")
    print(f"- Max 3D surface width: {properties.maximum_surface3d_width}")
    print(f"- Max 3D surface height: {properties.maximum_surface3d_height}")
    print(f"- Max 3D surface depth: {properties.maximum_surface3d_depth}")
    print(f"- Max cubemap surface width: {properties.maximum_surfacecubemap_width}")
    print(f"- Max layers in a cubemap layered surface: {properties.maximum_surfacecubemap_layered_layers}")
    print(f"- Max cubemap layered surface width: {properties.maximum_surfacecubemap_layered_width}")
    print(f"- Max 1D texture width: {properties.maximum_texture1d_width}")
    print(f"- Max width for a 1D texture bound to linear memory: {properties.maximum_texture1d_linear_width}")
    print(f"- Max layers in 1D layered texture: {properties.maximum_texture1d_layered_layers}")
    print(f"- Max 1D layered texture width: {properties.maximum_texture1d_layered_width}")
    print(f"- Max mipmapped 1D texture width: {properties.maximum_texture1d_mipmapped_width}")
    print(f"- Max 2D texture width: {properties.maximum_texture2d_width}")
    print(f"- Max 2D texture height: {properties.maximum_texture2d_height}")
    print(f"- Max width for a 2D texture bound to linear memory: {properties.maximum_texture2d_linear_width}")
    print(f"- Max height for a 2D texture bound to linear memory: {properties.maximum_texture2d_linear_height}")
    print(f"- Max pitch for a 2D texture bound to linear memory: \
          {_bytes_to_mbytes(properties.maximum_texture2d_linear_pitch)}")
    print(f"- Max layers in 2D layered texture: {properties.maximum_texture2d_layered_layers}")
    print(f"- Max 2D layered texture width: {properties.maximum_texture2d_layered_width}")
    print(f"- Max 2D layered texture height: {properties.maximum_texture2d_layered_height}")
    print(f"- Max mipmapped 2D texture width: {properties.maximum_texture2d_mipmapped_width}")
    print(f"- Max mipmapped 2D texture height: {properties.maximum_texture2d_mipmapped_height}")
    print(f"- Max 3D texture width: {properties.maximum_texture3d_width}")
    print(f"- Max 3D texture height: {properties.maximum_texture3d_height}")
    print(f"- Max 3D texture depth: {properties.maximum_texture3d_depth}")
    print(f"- Alternate max 3D texture width: {properties.maximum_texture3d_width_alternate}")
    print(f"- Alternate max 3D texture height: {properties.maximum_texture3d_height_alternate}")
    print(f"- Alternate max 3D texture depth: {properties.maximum_texture3d_depth_alternate}")
    print(f"- Max cubemap texture width or height: {properties.maximum_texturecubemap_width}")
    print(f"- Max layers in a cubemap layered texture: {properties.maximum_texturecubemap_layered_layers}")
    print(f"- Max cubemap layered texture width or height: {properties.maximum_texturecubemap_layered_width}")
    print(f"- Texture base address alignment requirement: {properties.texture_alignment}B")
    print(f"- Pitch alignment requirement for 2D texture references bound to pitched memory: \
          {properties.texture_pitch_alignment}B")
    print(f"- Support for memory pools: {_bool_str(properties.memory_pools_supported)}")
    print(f"- Bitmask of handle types supported with memory pool-based IPC: \
          0b{properties.mempool_supported_handle_types:032b}")
    print(f"- Multi-GPU board: {_bool_str(properties.multi_gpu_board)}")
    print(f"- Multi-GPU board group ID: {properties.multi_gpu_board_group_id}")
    print(f"- Support for switch multicast and reduction operations: {_bool_str(properties.multicast_supported)}")
    print(f"- Number of multiprocessors: {properties.multiprocessor_count}")
    print(f"- NUMA configuration: {properties.numa_config}")
    print(f"- NUMA node ID of GPU memory: {properties.numa_id}")
    print(f"- Support for coherently accessing pageable memory: {_bool_str(properties.pageable_memory_access)}")
    print(f"- Access pageable memory via host's page tables: \
          {_bool_str(properties.pageable_memory_access_uses_host_page_tables)}")
    print(f"- PCI bus ID: {properties.pci_bus_id}")
    print(f"- PCI device (slot) ID: {properties.pci_device_id}")
    print(f"- PCI domain ID: {properties.pci_domain_id}")
    print(f"- Support for registering memory that must be mapped to GPU as read-only: \
          {_bool_str(properties.read_only_host_register_supported)}")
    print(f"- Amount of shared memory per block reserved by CUDA driver: \
          {properties.reserved_shared_memory_per_block}B")
    print(f"- Support for sparse CUDA arrays and sparse CUDA mipmapped arrays: \
          {_bool_str(properties.sparse_cuda_array_supported)}")
    print(f"- Using TCC driver: {_bool_str(properties.tcc_driver)}")
    print(f"- Constant memory available: {properties.total_constant_memory}B")
    print(f"- Support for unified address space with host: {_bool_str(properties.unified_addressing)}")
    print(f"- Support for virtual memory management: {_bool_str(properties.virtual_memory_management_supported)}")


ndev = system.num_devices
print(f"Number of GPUs: {ndev}")

for device_id in range(ndev):
    device = Device(device_id)
    print(f"DEVICE {device.name} (id={device_id})")

    device.set_current()
    ctx = device.context

    cc = device.compute_capability
    prop = device.properties

    print(f"Device compute capability: major={cc[0]}, minor={cc[1]}")
    print(f"Architecture: sm_{cc[0]}{cc[1]}")
    print(f"PCI bus id={device.pci_bus_id}")
    print_device_properties(prop)
    print("*****************************************************\n\n")
