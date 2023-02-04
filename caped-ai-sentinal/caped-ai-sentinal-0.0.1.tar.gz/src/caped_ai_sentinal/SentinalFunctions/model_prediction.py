import os

import cellshape_helper as helper
import numpy as np
import pandas as pd
import torch
from cellshape_cloud import CloudAutoEncoder, PointCloudDataset
from cellshape_cluster import DeepEmbeddedClustering
from torch.utils.data import DataLoader
from tqdm import tqdm


class CloudAutoClusterPredict:
    def __init__(
        self,
        label_image_directory,
        cloud_model_directory,
        cloud_model_name,
        encoder_type,
        decoder_type,
        num_features,
        k_nearest_neighbours,
        num_points,
        gpu=True,
    ):
        self.label_image_directory = label_image_directory
        self.cloud_model_directory = cloud_model_directory
        self.cloud_model_name = cloud_model_name
        self.encoder_type = encoder_type
        self.decoder_type = decoder_type
        self.num_features = num_features
        self.k_nearest_neighbours = k_nearest_neighbours
        self.num_points = num_points
        self.gpu = gpu

    def _predict(self):
        autoencoder = CloudAutoEncoder(
            num_features=self.num_features,
            k=self.k_nearest_neighbours,
            encoder_type=self.encoder_type,
            decoder_type=self.decoder_type,
        )

        checkpoint = torch.load(
            os.path.join(self.cloud_model_directory, self.cloud_model_name)
        )
        num_clusters = checkpoint["model_state_dict"][
            "clustering_layer.weight"
        ].shape[0]

        print(f"The number of clusters in the loaded model is: {num_clusters}")

        model = DeepEmbeddedClustering(
            autoencoder=autoencoder, num_clusters=num_clusters
        )

        model.load_state_dict(checkpoint["model_state_dict"])

        # Move the model to the gpu if there is one available
        if self.gpu:
            device = torch.device("cuda:0")
        else:
            device = torch.device("cpu:0")
        model.to(device)

        # Put the model in evaluation mode
        model.eval()

        helper.label_tif_to_pc_directory(
            self.label_image_directory,
            self.cloud_model_directory,
            self.num_points,
        )
        dataset = PointCloudDataset(self.cloud_model_directory)
        dataloader = DataLoader(dataset, batch_size=1, shuffle=False)

        all_feat = []
        all_clusters = []
        all_outputs = []
        all_inputs = []
        for data in tqdm(dataloader):
            inputs = data[0]
            if self.gpu:
                output, features, clusters = model(inputs.cuda())
            else:
                output, features, clusters = model(inputs.cpu())
            all_feat.append(torch.squeeze(features).detach().cpu().numpy())
            all_clusters.append(torch.squeeze(clusters).detach().cpu().numpy())
            all_inputs.append(torch.squeeze(inputs).detach().cpu().numpy())
            all_outputs.append(torch.squeeze(output).detach().cpu().numpy())
            cluster_predictions = np.argmax(
                np.asarray(all_clusters).data, axis=1
            )
            folding_data = pd.DataFrame(np.asarray(all_feat))
            folding_data["cluster_labels"] = np.asarray(cluster_predictions)
