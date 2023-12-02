from bean.EdgeDataProcessor import EdgeDataProcessor

# Example Usage:
csv_file_path = "./dataset/edge-servers/site-optus-melbCBD.csv"
data_processor = EdgeDataProcessor(csv_file_path)
data_processor.process_data()
graph = data_processor.build_graph()
print(graph)
