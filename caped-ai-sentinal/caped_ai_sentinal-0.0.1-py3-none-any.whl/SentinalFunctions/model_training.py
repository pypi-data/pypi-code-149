import logging
from datetime import datetime

import torch
from cellshape_cloud import CloudAutoEncoder, PointCloudDataset, reports
from cellshape_cloud import train as cloudtrain
from cellshape_cloud.vendor.chamfer_distance import ChamferLoss
from cellshape_cluster import DeepEmbeddedClustering
from cellshape_cluster import train as clustertrain
from torch.utils.data import DataLoader


class CloudAutoCluster:
    def __init__(
        self,
        point_cloud_directory,
        cloud_model_directory,
        encoder_type,
        decoder_type,
        num_features,
        num_clusters,
        k_nearest_neighbours,
        batch_size,
        num_epochs,
        learning_rate,
        update_interval,
        gamma,
        divergence_tolerance,
    ):
        self.point_cloud_directory = point_cloud_directory
        self.cloud_model_directory = cloud_model_directory
        self.encoder_type = encoder_type
        self.decoder_type = decoder_type
        self.num_features = num_features
        self.num_clusters = num_clusters
        self.k_nearest_neighbours = k_nearest_neighbours
        self.batch_size = batch_size
        self.num_epochs = num_epochs
        self.learning_rate = learning_rate
        self.update_interval = update_interval
        self.gamma = gamma
        self.divergence_tolerance = divergence_tolerance
        self.logging_info = None

    def _train_autoencoder(self):
        autoencoder = CloudAutoEncoder(
            num_features=self.num_features,
            k=self.k_nearest_neighbours,
            encoder_type=self.encoder_type,
            decoder_type=self.decoder_type,
        )

        self.dataset = PointCloudDataset(self.point_cloud_directory)
        self.dataloader = DataLoader(
            self.dataset, batch_size=self.batch_size, shuffle=False
        )
        criterion = ChamferLoss()
        optimizer = torch.optim.Adam(
            autoencoder.parameters(),
            lr=self.learning_rate * 16 / self.batch_size,
            betas=(0.9, 0.999),
            weight_decay=1e-6,
        )

        (
            name_logging,
            name_model,
            name_writer,
            name,
        ) = reports.get_experiment_name(
            model=autoencoder, output_dir=self.cloud_model_directory
        )

        self.logging_info = name_logging, name_model, name_writer, name
        now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        logging.basicConfig(filename=name_logging, level=logging.INFO)
        logging.info(f"Started training model {name} at {now}.")

        output_cloud = cloudtrain(
            autoencoder,
            self.dataloader,
            self.num_epochs,
            criterion,
            optimizer,
            self.logging_info,
        )

        self.auto_encoder = output_cloud[0]

    def _train_clustering(self):
        model = DeepEmbeddedClustering(
            autoencoder=self.auto_encoder, num_clusters=self.num_clusters
        )

        dataloader = DataLoader(
            self.dataset, batch_size=self.batch_size, shuffle=False
        )
        # it is very important that shuffle=False here!
        dataloader_inf = DataLoader(self.dataset, batch_size=1, shuffle=False)
        # it is very important that batch_size=1 and shuffle=False here!

        optimizer = torch.optim.Adam(
            model.parameters(),
            lr=self.learning_rate * 16 / self.batch_size,
            betas=(0.9, 0.999),
            weight_decay=1e-6,
        )

        reconstruction_criterion = ChamferLoss()
        cluster_criterion = torch.nn.KLDivLoss(reduction="sum")

        clustertrain(
            model,
            dataloader,
            dataloader_inf,
            self.num_epochs,
            optimizer,
            reconstruction_criterion,
            cluster_criterion,
            self.update_interval,
            self.gamma,
            self.divergence_tolerance,
            self.logging_info,
        )
